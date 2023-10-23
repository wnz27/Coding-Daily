/*
 * @Author: 27
 * @LastEditors: 27
 * @Date: 2023-10-23 09:49:24
 * @LastEditTime: 2023-10-23 16:16:10
 * @FilePath: /Coding-Daily/content/examples/operator/operator-new/internal/controller/bizserver_controller.go
 * @description: type some description
 */
/*
Copyright 2023.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

package controller

import (
	"context"

	"github.com/go-logr/logr"
	appsv1 "k8s.io/api/apps/v1"
	"k8s.io/apimachinery/pkg/api/errors"
	"k8s.io/apimachinery/pkg/runtime"
	ctrl "sigs.k8s.io/controller-runtime"
	"sigs.k8s.io/controller-runtime/pkg/client"
	"sigs.k8s.io/controller-runtime/pkg/log"

	backendv1 "tutorial.kubebuilder.io/operator-new/api/v1"
	"tutorial.kubebuilder.io/operator-new/internal/common"
)

// BizServerReconciler reconciles a BizServer object
type BizServerReconciler struct {
	client.Client
	Scheme *runtime.Scheme
	Log    logr.Logger
}

//+kubebuilder:rbac:groups=backend.tutorial.kubebuilder.io,resources=bizservers,verbs=get;list;watch;create;update;patch;delete
//+kubebuilder:rbac:groups=backend.tutorial.kubebuilder.io,resources=bizservers/status,verbs=get;update;patch
//+kubebuilder:rbac:groups=backend.tutorial.kubebuilder.io,resources=bizservers/finalizers,verbs=update

// Reconcile is part of the main kubernetes reconciliation loop which aims to
// move the current state of the cluster closer to the desired state.
// TODO(user): Modify the Reconcile function to compare the state specified by
// the BizServer object against the actual cluster state, and then
// perform operations to make the cluster state reflect the state specified by
// the user.
//
// For more details, check Reconcile and its Result here:
// - https://pkg.go.dev/sigs.k8s.io/controller-runtime@v0.16.0/pkg/reconcile
func (r *BizServerReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {
	_ = log.FromContext(ctx)

	// TODO(user): your logic here
	_ = r.Log.WithValues("apiexamplea", req.NamespacedName)

	// 获取当前的 CR，并打印
	obj := &backendv1.BizServer{}
	if err := r.Get(ctx, req.NamespacedName, obj); err != nil {
		r.Log.Error(err, "Unable to fetch object")
	} else {
		r.Log.Info("Geeting from Kubebuilder to", obj.Spec.Image, obj.Spec.MysqlSecret)
	}

	// 查询 deployment
	serverDeployment := &appsv1.Deployment{}
	if err := r.Get(ctx, client.ObjectKey{
		Namespace: obj.NameSpace(), Name: obj.ServerName()}, serverDeployment); err != nil {
		if errors.IsNotFound(err) {
			// 如果 Deployment 不存在，创建一个新的 Deployment
			// 构造 deployment
			r.Log.Info("new deployment", "server name", obj.ServerName())
			serverDeployment = common.NewDeployment(ctx,
				obj.ServerName(),
				obj.ServerImage(),
				obj.MysqlSecret(),
				obj.NameSpace(),
				obj.Replicas(),
				obj.MatchLabels(),
				obj.LimitCPU(),
				obj.LimitMemory(),
				obj.ReqCPU(),
				obj.ReqMemory(),
			)
			// 部署 deployment
			if err := r.Create(ctx, serverDeployment); err != nil {
				return ctrl.Result{}, err
			}
		}
		return ctrl.Result{}, err
	}

	// 如果 Deployment 已存在，检查镜像和配置是否需要更新
	// TODO 判断 config 是否 变更
	// TODO 判断 secret 是否变更
	if serverDeployment.Spec.Template.Spec.Containers[0].Image != obj.ServerImage() {
		// 更新 Deployment
		newDeployment := common.NewDeployment(ctx,
			obj.ServerName(),
			obj.ServerImage(),
			obj.MysqlSecret(),
			obj.NameSpace(),
			obj.Replicas(),
			obj.MatchLabels(),
			obj.LimitCPU(),
			obj.LimitMemory(),
			obj.ReqCPU(),
			obj.ReqMemory(),
		)
		if err := r.Update(ctx, newDeployment); err != nil {
			return ctrl.Result{}, err
		}
	}

	// service
	r.Log.Info("new service", "service name", obj.ServiceName())
	newService := common.BuildService(obj.ServiceName(), obj.NameSpace(), obj.MatchLabels())
	// 部署 service
	if err := r.Create(ctx, &newService); err != nil {
		return ctrl.Result{}, err
	}

	// virtualservice
	r.Log.Info("new virtual service", "server name", obj.VirtualServiceName())
	newVirtualService := common.BuildVirtualService(obj.NameSpace(), obj.VirtualServiceName())
	if err := r.Create(ctx, &newVirtualService); err != nil {
		return ctrl.Result{}, err
	}

	// 初始化 CR 的 Status 为 Running
	obj.Status.Status = "Running"
	if err := r.Status().Update(ctx, obj); err != nil {
		r.Log.Error(err, "unable to update status")
	}

	r.Log.Info("done deploy", "server", obj.ServerName())

	return ctrl.Result{Requeue: true}, nil
}

// SetupWithManager sets up the controller with the Manager.
func (r *BizServerReconciler) SetupWithManager(mgr ctrl.Manager) error {
	return ctrl.NewControllerManagedBy(mgr).
		For(&backendv1.BizServer{}).
		Complete(r)
}
