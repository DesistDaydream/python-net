# 概述

requests 包的封装，以便对多种请求进行统一处理（e.g. 统一的请求头、请求参数、等）以简化代码。

简单点说就是用 Python 写某个服务的 sdk，或者说某个服务的 API。写成后，可以让人直接调用。最常见的就是各种公有云的 OpenAPI。

以青龙 API 的封装为例。