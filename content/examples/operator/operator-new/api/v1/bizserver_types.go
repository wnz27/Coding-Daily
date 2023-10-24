/*
 * @Author: 27
 * @LastEditors: 27
 * @Date: 2023-10-23 09:49:24
 * @LastEditTime: 2023-10-24 11:03:30
 * @FilePath: /Coding-Daily/content/examples/operator/operator-new/api/v1/bizserver_types.go
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

package v1

import (
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
)

// EDIT THIS FILE!  THIS IS SCAFFOLDING FOR YOU TO OWN!
// NOTE: json tags are required.  Any new fields you add must have json tags for the fields to be serialized.

// BizServerSpec defines the desired state of BizServer
type BizServerSpec struct {
	// INSERT ADDITIONAL SPEC FIELDS - desired state of cluster
	// Important: Run "make" to regenerate code after modifying this file

	// Foo is an example field of BizServer. Edit bizserver_types.go to remove/update
	ServerName         string `json:"server_name"`
	NameSpace          string `json:"namespace"`
	Image              string `json:"image"`
	MysqlSecret        string `json:"mysql_secret"`
	PublicConfig       string `json:"public_config"`
	ServiceName        string `json:"service_name"`
	VirtualServiceName string `json:"virtual_service_name"`
	Replicas           int32  `json:"replicas,omitempty"`
	LimitCPU           string `json:"limit_cpu,omitempty"`
	LimitMemory        string `json:"limit_memory,omitempty"`
	ReqCPU             string `json:"req_cpu,omitempty"`
	ReqMemory          string `json:"req_memory,omitempty"`
	VirtualServiceHost string `json:"virtual_service_host"`
}

// BizServerStatus defines the observed state of BizServer
type BizServerStatus struct {
	// INSERT ADDITIONAL STATUS FIELD - define observed state of cluster
	// Important: Run "make" to regenerate code after modifying this file
	Status string `json:"status"`
}

//+kubebuilder:object:root=true
//+kubebuilder:subresource:status

// BizServer is the Schema for the bizservers API
type BizServer struct {
	metav1.TypeMeta   `json:",inline"`
	metav1.ObjectMeta `json:"metadata,omitempty"`

	Spec   BizServerSpec   `json:"spec,omitempty"`
	Status BizServerStatus `json:"status,omitempty"`
}

// Getter to virtual service host
func (s *BizServer) VirtualServiceHost() string {
	return s.Spec.VirtualServiceHost
}

// Getter to  replicas
func (s *BizServer) Replicas() int32 {
	r := s.Spec.Replicas
	if r == 0 {
		return 1
	}
	return r
}

func (s *BizServer) MatchLabels() map[string]string {
	return map[string]string{
		"app.kubernetes.io/name": s.ServerName(),
	}
}

// Getter to limit cpu, default is 50m
func (s *BizServer) LimitCPU() string {
	l := s.Spec.LimitCPU
	if l == "" {
		return "50m"
	}
	return l
}

// Getter to limit memory, default is 50Mi
func (s *BizServer) LimitMemory() string {
	l := s.Spec.LimitMemory
	if l == "" {
		return "50Mi"
	}
	return l
}

// Getter to req cpu, default is 25m
func (s *BizServer) ReqCPU() string {
	r := s.Spec.ReqCPU
	if r == "" {
		return "25m"
	}
	return r
}

// Getter to req memory, default is 25Mi
func (s *BizServer) ReqMemory() string {
	r := s.Spec.ReqMemory
	if r == "" {
		return "25Mi"
	}
	return r
}

func (s *BizServer) ServiceName() string {
	return s.Spec.ServiceName
}

func (s *BizServer) ServerName() string {
	return s.Spec.ServerName
}

func (s *BizServer) VirtualServiceName() string {
	return s.Spec.VirtualServiceName
}

func (s *BizServer) ServerImage() string {
	return s.Spec.Image
}

// Getter to  mysql secret
func (s *BizServer) MysqlSecret() string {
	return s.Spec.MysqlSecret
}

// Getter to public config
func (s *BizServer) PublicConfig() string {
	return s.Spec.PublicConfig
}

// Getter to namespace
func (s *BizServer) NameSpace() string {
	return s.Spec.NameSpace
}

//+kubebuilder:object:root=true

// BizServerList contains a list of BizServer
type BizServerList struct {
	metav1.TypeMeta `json:",inline"`
	metav1.ListMeta `json:"metadata,omitempty"`
	Items           []BizServer `json:"items"`
}

func init() {
	SchemeBuilder.Register(&BizServer{}, &BizServerList{})
}
