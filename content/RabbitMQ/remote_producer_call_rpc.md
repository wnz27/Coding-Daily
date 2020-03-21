<!--
 * @Author: 27
 * @LastEditors: 27
 * @Date: 2020-01-20 10:59:03
 * @LastEditTime: 2020-03-21 17:20:16
 * @FilePath: /Coding-Daily/content/RabbitMQ/remote_producer_call_rpc.md
 * @description: type some description
 -->
[回到目录](../../README.md)
---

## note on RPC
Bearing that in mind, consider the following advice:
- Make sure it's obvious which function call is local and which is remote.
- Document your system. Make the dependencies between components clear.
- Handle error cases. How should the client react when the RPC server is down for a long time?

