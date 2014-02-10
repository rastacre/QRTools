var div = document.getElementById("qrgen_cont");
if (div == null){
	function qr(url){
	d = document.createElement("div");
	d.id = "qrgen_cont";
	d.style.cssText="-webkit-border-radius:20px 0 20px 20px;;-moz-border-radius:20px 0 20px 20px;border-top:2px solid;border-right:2px solid;border-left:9px solid;border-bottom:9px solid;height:250px;margin:0;padding:10px;position:fixed;right:0px;top:0px;width:250px;background:none repeat scroll 0 0 white;z-index:9999;"
	cbutton =	"data:image/png;base64,"+
				"iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz" + 
				"AAALEgAACxIB0t1+/AAAACB0RVh0U29mdHdhcmUATWFjcm9tZWRpYSBGaXJld29ya3MgTVi7kSok" + 
				"AAAAFnRFWHRDcmVhdGlvbiBUaW1lADExLzA1LzA33bqJ2wAAAtJJREFUeJxlk0toXGUUx3/fdzuP" + 
				"Os+kusrgpuTVmLZgUoO46KIqKoREzKKb4KKb7MVFF5YKddGVCLr0AWKhiybLSkppRLFoCXaSSdKM" + 
				"QokTu2nmPdOZe+93jotJZYIHDgfO48+B3zlGVem3/Lvjp000ehXrTan1ciIO8bsl8bsP1O9emb73" + 
				"d76/3/QLbM6fXcZ6c50newS1Cs65XsF6eIkkJjMIYbgyc29v/ojA3vWP4o3f14pB5WmuVXqMU3CA" + 
				"Hro5dA+w2RMQi5faL+aG37p1v2MB6r/euRFUnuaapccECpLM4it0BXzpRUmk8RXC6gGu3crF//nr" + 
				"BoDZ/GBqWkV+qxXWCRRGPvuaxMgkPy9eIGjUAIim0rz2xU0aj/IUr39MxIDLnMConrPS7VzrPNnD" + 
				"KZDMkBw/S3rsDDPf3EaTGTSZ4dyXt0gNT/DCyVO04ylCBdtuomFwzWwsTJcahfWhTujwld7At3fI" + 
				"jpziYHMdnCN7cpTy9kPuLi3AswYDHkStwY+n9q2IDjnnUEAUuvUaa4sXKO/kGRybZGD0Fcq7BX5c" + 
				"WiBoNThuQBVQJRQZOibSQ/UcpgIYg+mHrWCNIWKPpFBxWAnDfaz330A0neX8d6sMjJ2mvLPBwaNN" + 
				"BkcnePOrm0ST6T5hgzi3b6Xd3PISSQwQzWR54/u7ZMfPUN7Jc/vD91i9NEtlt8DA8ASvf/4DkVQa" + 
				"ayA0hmPitqx6kcsmM4gHaL1KY/sPKtsPWV18G23VibTr/LL0PtVigeqfWzTrdSzQUYMTuWxUlfvn" + 
				"X14On7XnwuoBgUKQyFCr1zhuni8LkWSKZqNBxEDMs4SiK7NFmbcAfm74IrF4yaSyRAxEWzUyFqIG" + 
				"YqYXvXYPX8yz+KKlkq8X//dMP828tByIzvWOxAfVQzqG0Bg6ajAiK7NFOfpM/bb2amYyVD4NRacC" + 
				"0ZyKA+dKRtwDT+WTd3Zlo7//X9Bdcywg+WD0AAAAAElFTkSuQmCC";
	c = document.createElement("div");
	c.id = "qrgen_close";
	c.style.cssText="background:url(" + cbutton + ") no-repeat 0 0 white;border: 4px solid;border-radius: 20px;height: 16px;margin: 0;min-width: 0;padding: 0;position: fixed;right: 251px;top: 251px;width: 16px;z-index: 9999;"

	i = document.createElement("img");
i.src="http://qr-tools.appspot.com/qr?url="+encodeURIComponent(url);
	i.alt=url
	i.title=url
	i.onclick=function(){document.getElementsByTagName('body')[0].removeChild(document.getElementById('qrgen_cont'));}
	c.onclick=function(){document.getElementsByTagName('body')[0].removeChild(document.getElementById('qrgen_cont'));}
	d.appendChild(i)
	d.appendChild(c)
	
	document.getElementsByTagName("body")[0].appendChild(d);
	}
	
	
	qr(location.href)
}
