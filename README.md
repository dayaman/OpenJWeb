# OpenJWeb

## Overview

これは、[OpenJTalk](http://open-jtalk.sourceforge.net/)のWebAPIサーバープログラムです。

## Description
[OpenJTalk](http://open-jtalk.sourceforge.net/)の読み上げ機能を用いて、文章をwav音声に変換する、WebAPIサーバープログラムです。  


## Requirement
 - python3.9.4
 - flask
 - open-jtalk
 - open-jtalk-mecab-naist-jdic

## Usage
### POST /
#### Parameters
|  Name  | Required |  Type  | Description |
| ------ | -------- | ------ | ----------- |
| `text` | required | string | 読み上げる文章 |

## Install
### Use DockerCompose
1. `$ docker-compose up`  

デフォルトでは、[HTS voice tohoku-f01](https://github.com/icn-lab/htsvoice-tohoku-f01.git)が音声として設定されます。