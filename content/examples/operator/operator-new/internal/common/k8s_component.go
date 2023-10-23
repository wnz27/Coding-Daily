/*
 * @Author: 27
 * @LastEditors: 27
 * @Date: 2023-10-23 10:03:13
 * @LastEditTime: 2023-10-23 17:24:54
 * @FilePath: /Coding-Daily/content/examples/operator/operator-new/internal/common/k8s_component.go
 * @description: type some description
 */
package common

import (
	"context"

	networkingv1alpha3 "istio.io/api/networking/v1alpha3"
	istio "istio.io/client-go/pkg/apis/networking/v1alpha3"
	appsv1 "k8s.io/api/apps/v1"
	corev1 "k8s.io/api/core/v1"
	"k8s.io/apimachinery/pkg/api/resource"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/apimachinery/pkg/util/intstr"
)

// 创建 deployment
func NewDeployment(ctx context.Context,
	deployName, imageName,
	mysqlSecret,
	nameSpace string,
	raplicas int32,
	matchLabels map[string]string,
	limitCpu, limitMemory, reqCpu, reqMemory string,
) *appsv1.Deployment {

	// 创建一个新的 Container
	c := buildContainer("test-demo-server", imageName,
		buildContainerPorts(),
		[]corev1.VolumeMount{},
		[]corev1.EnvVar{{Name: "CONTAINER_ENV", Value: "test"}},
		buildEnvFrom(),
		limitCpu, limitMemory, reqCpu, reqMemory,
	)
	// 创建一个新的 Deployment
	deployment := &appsv1.Deployment{
		ObjectMeta: metav1.ObjectMeta{
			Name:      deployName,
			Namespace: nameSpace,
		},
		// 配置 Deployment 规范，包括 Pod 模板
		Spec: buildDeploySpec(raplicas, matchLabels, c),
	}

	// 设置 ConfigMap 的挂载 暂时无用
	// deployment.Spec.Template.Spec.Containers[0].VolumeMounts = []corev1.VolumeMount{
	// 	{
	// 		Name:      "domains-public-volume",
	// 		SubPath:   "domains_public.yaml",
	// 		MountPath: "image/path/want", // 镜像里要放置的位置 跟 Dockerfile 服务使用的情况有关
	// 	},
	// }

	return deployment
}

func buildDeploySpec(replicas int32, matchLabels map[string]string, container corev1.Container) appsv1.DeploymentSpec {
	return appsv1.DeploymentSpec{
		Replicas: &replicas,
		Selector: &metav1.LabelSelector{
			MatchLabels: matchLabels,
		},
		Template: corev1.PodTemplateSpec{
			ObjectMeta: metav1.ObjectMeta{
				Labels: matchLabels,
			},
			Spec: corev1.PodSpec{
				Containers: []corev1.Container{container},
				// 暂时无用
				Volumes: []corev1.Volume{
					{Name: "domains-public-volume",
						VolumeSource: corev1.VolumeSource{ConfigMap: &corev1.ConfigMapVolumeSource{LocalObjectReference: corev1.LocalObjectReference{Name: "domains-public-config"}}}},
				},
			},
		},
	}
}

// envs 暂无用
func buildContainer(
	name, image string, ports []corev1.ContainerPort,
	volumeMounts []corev1.VolumeMount,
	envs []corev1.EnvVar, // []corev1.EnvVar{	{Name: "CONTAINER_ENV", Value: "test"},}
	envFrom []corev1.EnvFromSource,
	limitCpu, limitMemory, reqCpu, reqMemory string,
) corev1.Container {
	// TODO 获取 port 中的健康检查接口
	liveProbe := buildLivenessOrReadinessPorbe("http", "/helloworld/liveprobe")

	return corev1.Container{
		Name: name,
		// 设置容器镜像
		Image:           image,
		ImagePullPolicy: corev1.PullPolicy("IfNotPresent"),
		Env:             envs,
		EnvFrom:         envFrom,
		Ports:           ports,
		VolumeMounts:    volumeMounts, // TODO 暂无用 传空 需配合 Spec 的 Volumes
		Resources:       buildResources(limitCpu, limitMemory, reqCpu, reqMemory),
		LivenessProbe:   &liveProbe,
		ReadinessProbe:  &liveProbe,
	}
}

func buildEnvFrom() []corev1.EnvFromSource {
	// TODO 参数 + 构建逻辑 names + types 11 对应就行
	return []corev1.EnvFromSource{
		{
			ConfigMapRef: &corev1.ConfigMapEnvSource{
				LocalObjectReference: corev1.LocalObjectReference{Name: "domains-public-config"},
			},
		},
		{
			SecretRef: &corev1.SecretEnvSource{
				LocalObjectReference: corev1.LocalObjectReference{Name: "mysql-test"},
			},
		},
	}
}

func buildContainerPorts() []corev1.ContainerPort {
	// TODO 参数 + 构建逻辑
	return []corev1.ContainerPort{
		{
			Name:          "http",
			ContainerPort: 8000,
			Protocol:      corev1.ProtocolTCP,
		},
		{
			Name:          "grpc",
			ContainerPort: 9000,
			Protocol:      corev1.ProtocolTCP,
		},
	}
}

func buildResources(limitCpu, limitMemory, reqCpu, reqMemory string) corev1.ResourceRequirements {
	return corev1.ResourceRequirements{
		Requests: corev1.ResourceList{
			// corev1.ResourceCPU:    resource.MustParse("25m"),
			corev1.ResourceCPU: resource.MustParse(reqCpu),
			// corev1.ResourceMemory: resource.MustParse("25M"),
			corev1.ResourceMemory: resource.MustParse(reqMemory),
		},
		Limits: corev1.ResourceList{
			// corev1.ResourceCPU:    resource.MustParse("50m"),
			corev1.ResourceCPU: resource.MustParse(limitCpu),
			// corev1.ResourceMemory: resource.MustParse("50M"),
			corev1.ResourceMemory: resource.MustParse(limitMemory),
		},
	}
}

func buildLivenessOrReadinessPorbe(portName, healthzCheckPath string) corev1.Probe {
	return corev1.Probe{
		ProbeHandler: corev1.ProbeHandler{
			HTTPGet: &corev1.HTTPGetAction{
				Port: intstr.IntOrString{
					Type:   intstr.String,
					StrVal: portName, // 跟 container 的 port 的 name一致
				},
				Path: healthzCheckPath, // 服务的 健康检查接口 如 /healthz
			},
		},
		InitialDelaySeconds: 120,
		PeriodSeconds:       5,
		TimeoutSeconds:      1,
		SuccessThreshold:    1,
		FailureThreshold:    3,
	}
}

// 创建 service
func BuildService(serviceName, nameSpace string, matchLabels map[string]string) corev1.Service {
	return corev1.Service{
		ObjectMeta: metav1.ObjectMeta{
			Name:      serviceName,
			Namespace: nameSpace,
			Labels:    matchLabels,
		},
		Spec: corev1.ServiceSpec{
			Selector: matchLabels,
			Ports:    buildServicePort(),
		},
	}
}

func buildServicePort() []corev1.ServicePort {
	return []corev1.ServicePort{
		{
			Name:     "http-svc",
			Protocol: corev1.ProtocolTCP,
			Port:     8000,
			TargetPort: intstr.IntOrString{
				Type:   intstr.Int,
				IntVal: 8000,
			},
		},
		{
			Name:     "rpc-svc",
			Protocol: corev1.ProtocolTCP,
			Port:     9000,
			TargetPort: intstr.IntOrString{
				Type:   intstr.Int,
				IntVal: 9000,
			},
		},
	}
}

// 创建 vs
func BuildVirtualService(nameSpace, virtualServiceName string) istio.VirtualService {
	uri := networkingv1alpha3.StringMatch_Prefix{Prefix: "/"}
	// 创建 VirtualService
	return istio.VirtualService{
		ObjectMeta: metav1.ObjectMeta{
			Name:      virtualServiceName,
			Namespace: nameSpace,
		},
		Spec: networkingv1alpha3.VirtualService{
			Hosts:    []string{"server-demo.newtest.internal.guanmai.cn"}, // 定义主机
			Gateways: []string{"istio-system/istio-gateway-internal"},     // 关联到 Istio 网关
			Http: []*networkingv1alpha3.HTTPRoute{
				{
					Match: []*networkingv1alpha3.HTTPMatchRequest{
						{
							Uri: &networkingv1alpha3.StringMatch{
								MatchType: &uri,
							},
						},
					},
					Route: []*networkingv1alpha3.HTTPRouteDestination{
						{
							Destination: &networkingv1alpha3.Destination{
								Host: virtualServiceName, // 与你的 Service 名称匹配
								Port: &networkingv1alpha3.PortSelector{
									Number: 8000, // 与 Service 暴露的端口匹配
								},
							},
						},
					},
				},
			},
		},
	}
}
