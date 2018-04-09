<?php

namespace App\Handlers;

use GuzzleHttp\Client;
use Overtrue\Pinyin\Pinyin;

class SlugTranslateHandler
{
    private $api = 'http://api.fanyi.baidu.com/api/trans/vip/translate?';
    private $app_id;
    private $key;
    private $text;

    public function __construct($text, $app_id, $key)
    {
        $this->text = $text;
        $this->app_id = $app_id;
        $this->key = $key;
    }
    public function translate($text)
    {

        // 如果没有配置百度翻译，自动使用兼容的拼音方案
        if (empty($this->app_id) || empty($this->key)) {
            return $this->pinyin($text);
        }

        $http = new Client;

        // 发送 HTTP Get 请求
        $response = $http->get($this->str_query());

        $result = json_decode($response->getBody(), true);

        // 尝试获取获取翻译结果
        if (isset($result['trans_result'][0]['dst'])) {
            return str_slug($result['trans_result'][0]['dst']);
        } else {
            // 如果百度翻译没有结果，使用拼音作为后备计划。
            return $this->pinyin($text);
        }
    }

    private function pinyin($text)
    {
        return str_slug(app(Pinyin::class)->permalink($text));
    }

    private function str_query()
    {
        $salt = time();
        $sign = md5($this->app_id . $this->text . $salt . $this->key);
        // 构建请求参数
        $query = http_build_query([
            "q"     =>  $this->text,
            "from"  => "zh",
            "to"    => "en",
            "appid" => $this->app_id,
            "salt"  => $salt,
            "sign"  => $sign,
        ]);

        return $this->api . $query;
    }
}
