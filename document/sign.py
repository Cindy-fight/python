"""

签名测试：

public function actionCheck(){

//     	http://sms.yy39wt.com/pay-sms-access/getPassageWayInfoApi.json?
// mobile=15760254214&imsi=460077568293535&imei=864615036105278&iccid=898600a5221601473535&ip=117.177.78.252&price=1000&orderNo=TeLhpHTc1l&merchantId=10160
// &appId=100565¬ifyUrl=http%3A%2F%2Fdata.maimob.cn%2Findex.php%2FOut%2FCMP%2Fss%2FXZpc3UbRE0&provinceCode=5&sign=7023C1001FB29C7B4B1B86F3241ACF34

    	$params = array(
    			'imsi'	=> '460077568293535',
    			'imei'	=> '864615036105278',
    			'iccid'	=> '898600a5221601473535',
    			'provinceCode'	=> '5',
    			'price' => 1000,
    			'orderNo'	=> 'TeLhpHTc1l',
    			'merchantId'	=> '10160',
    			'appId'		=> '100565',
    	);

    	$cp = ksort($params);
    	var_dump($params);
    	$c = http_build_query($params).'AAB3C9FA1DFD18BF914D587257DF1A2F';
    	$sign = strtoupper(md5($c));
    	var_dump($c);
    	var_dump($sign);


    	$dataKeys   = explode(',', 'appId,iccid,imei,imsi,merchantId,orderNo,price,provinceCode,@=AAB3C9FA1DFD18BF914D587257DF1A2F');
    	$retArr1 = [];
    	$retArr2 = [];
    	foreach ($dataKeys as $dataKey){
    		if(substr($dataKey,0,1) == '@'){
    			$tmp    = explode('=', substr($dataKey,1));
    			$retArr1[$tmp[0]]    = $tmp[1];
    		}else{
    			if(strlen($params[$dataKey]) > 0){
    				$retArr1[$dataKey]   = $params[$dataKey];
    			}
    		}
    	}
    	foreach ($retArr1 as $pkey => $pval){
    		if($pkey != ''){
    			$retArr2[]  = $pkey.'='.$pval;
    		}else{
    			$retArr2[]  = $pkey.$pval;
    		}
    	}
    	$ret    = implode('&', $retArr2);
    	$ret    = md5($ret);
    	echo strtoupper($ret);



    }



"""