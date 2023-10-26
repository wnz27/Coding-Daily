/*
 * @Author: 27
 * @LastEditors: 27
 * @Date: 2023-10-21 20:07:02
 * @LastEditTime: 2023-10-26 14:46:03
 * @FilePath: /Coding-Daily/content/examples/serverdemo/internal/service/greeter.go
 * @description: type some description
 */
package service

import (
	"context"
	"os"

	v1 "serverdemo/api/helloworld/v1"
	"serverdemo/internal/biz"
)

// GreeterService is a greeter service.
type GreeterService struct {
	v1.UnimplementedGreeterServer

	uc *biz.GreeterUsecase
}

// NewGreeterService new a greeter service.
func NewGreeterService(uc *biz.GreeterUsecase) *GreeterService {
	return &GreeterService{uc: uc}
}

// SayHello implements helloworld.GreeterServer.
func (s *GreeterService) SayHello(ctx context.Context, in *v1.HelloRequest) (*v1.HelloReply, error) {
	g, err := s.uc.CreateGreeter(ctx, &biz.Greeter{Hello: in.Name})
	if err != nil {
		return nil, err
	}
	// 获取配置
	// 从 环境变量获取信息
	user_name := os.Getenv("username")
	config1 := os.Getenv("domains_public.yaml")
	msg := "Hello " + g.Hello + " " + user_name + " " + config1
	return &v1.HelloReply{Message: msg}, nil
}
