(function(){var u=Math.random()<_atc.famp,C=_ate,A=document,p=window,g={},o={},x={},r={};function t(w,d,a){w/=d;w=Math.round(w*10)/10;if((w+"").length>4){w=Math.round(w);}return w+a;}function m(a){var d=(""+a).split(".").shift().length;if(isNaN(a)){return a;}else{if(d<4){return Math.round(a);}else{if(d<7){return t(a,1000,"K");}else{if(d<10){return t(a,1000000,"M");}else{return t(a,1000000000,"B");}}}}}function s(d){try{if(p.JSON&&p.JSON.parse){return JSON.parse(d);}}catch(a){return{};}}function q(d){try{if(p.JSON&&p.JSON.stringify){return JSON.stringify(d);}}catch(a){return"";}}function j(d){var a=_ate.cookie.rck("_atshc");if(a){return(s(a)||{})[d]||-1;}return-1;}function e(d,w){var a=_ate.cookie.rck("_atshc"),E;if(a){a=s(a);E=(a||{})[d]||0;if(E&&w>=E){delete a[d];_ate.cookie.sck("_atshc",q(a),1,1);}}}function B(d){var a=_ate.cookie.rck("_atshc"),w=D(d)+1;d.shares=w;y(d,m(w));if(!a){a={};}else{a=s(a);}if(a[d.url]){delete a[d.url];}o[d.url]=a[d.url]=w;_ate.cookie.sck("_atshc",q(a),1,1);}function D(a){var d=0;if(a&&a.shares){d=a.shares;if(isNaN(d)){d=0;}}return d;}function y(a,K){if(!a){return;}var O=a.className.indexOf("pill_style")>-1,L=(parseInt(K)!==0),G=!a.firstChild,M=a.addthis_conf||{},N=a.addthis_share||{};if(a.firstChild&&a.firstChild.nodeType==3){a.removeChild(a.firstChild);}if(G){var F=A.ce("a"),w=A.ce("a"),d=A.ce("span"),J=A.createTextNode("Share"),H=(document.compatMode=="BackCompat"),E=[],I;a.style.display="none";F.className="addthis_button_expanded";w.className="atc_s addthis_button_compact";w.appendChild(d);if(L&&O){a.className+=" addthis_nonzero";}if(H&&_ate.bro.msi&&O){F.style.lineHeight="20px";}M.ui_offset_top=(_ate.bro.msi?0:20)+(_ate.bro.ffx&&!H?15:0);M.ui_offset_left=0;M.product="sco"+(O?"pl":"")+"-"+_ate.ver();if(O){E=[w,F];}else{E=[F,w];}while(I=E.shift()){a.appendChild(I);}addthis.button(w,M,N);addthis._render([F],{conf:M,share:N},{nohover:true,singleservice:M.service||"more"});}K=A.createTextNode(K);if(!O){if(a.firstChild&&a.firstChild.firstChild){a.firstChild.removeChild(a.firstChild.firstChild);}(a.firstChild)?a.firstChild.appendChild(K):a.appendChild(K);}else{if(a.firstChild&&a.firstChild.nextSibling&&a.firstChild.nextSibling.firstChild){a.firstChild.nextSibling.removeChild(a.firstChild.nextSibling.firstChild);}if(!L){if(a.className){a.className=a.className.replace(/addthis_nonzero/g,"");}}else{if(a.className.indexOf("addthis_nonzero")==-1){a.className+=" addthis_nonzero";}a.firstChild.nextSibling.appendChild(K);}}if(_ate.bro.ie6||_ate.bro.ie7||_ate.bro.ff2||_ate.bro.opr){a.style.display="block";}else{a.style.display="inline-block";}a.href="#";}function c(a,d){a.shares=d;y(a,m(d));}function n(d,F,G,a){var w=0,E=j(d.url);if(F.error){w="?";}else{w=F.shares;}if(!isNaN(E)&&((isNaN(w)&&E>0)||E>w)){w=E;}else{e(d.url,w);}if(!o[d.url]){o[d.url]=w;}if(a){G(d,F);}else{G(d,w);}}function b(d,E){if(!d){E({error:{message:"no url provided",code:-10}});}if(r[d]){E(r[d]);}var a=d,w=_ate.util.scb("sc",d,function(G){if(u){var H=((new Date()).getTime()-_ate.cbs["time_"+w]),F=new Image();C.imgz.push(F);F.src="//m.addthisedge.com/live/t00/mu.gif?a=sc&r="+(1/u)+"&"+(isNaN(H)?"err=1":"t="+H);}if(!G.url){G.url=d;}r[d]=G;E(r[d]);},function(){r[d]={error:{message:"server timed out",code:999}};E(r[d]);});a=C.util.gUD(d).toLowerCase()+C.util.gUQS(d);_ate.ajs("//api-public.addthis.com/url/shares.json?url="+_euc(a)+"&callback="+w,1);}function z(d,F,a){var E=j(d.url),w=d.url;if(!x[w]){x[w]=[];}x[w].push(d);_ate.ed.addEventListener("addthis.menu.share",function(G){try{if(G.data.service&&_ate.track.mgu(G.data.url,{clean:1,defrag:1})==w){if(G.data.service=="facebook_unlike"||(_ate.ver()>=300&&(G.data.service=="more"||G.data.service=="email"))||G.data.service=="google_unplusone"){return;}B(d);}}catch(G){}});if(o[w]!==undefined){F(d,o[w]);}else{if(w){if(!isNaN(E)&&E>0){F(d,E);}_ate.track.apc("sco"+(d.className.indexOf("pill_style")>-1?"pl":"")+"-"+_ate.ver());if(x[w].length>1){return;}b(w,function(H){if(H&&!H.error&&H.shares){o[w]=H.shares;}if(x[w]){for(var G=0;G<x[w].length;G++){n(x[w][G],H,F);}}});}}}var h={services:{facebook:{cb:function(d){var w=d.params,a=d.data;if(a.data.length){d.callbackFunc({elem:w.elem,service:w.service,countUrl:w.countUrl,count:a.data[0].total_count,share:a.data[0]});}},ajs:function(a){var d=a.params,w=a.cbname;_ate.ajs(this.baseUrl+_euc(d.countUrl)+"\"&"+this.jsonpParam+"="+w,1);},baseUrl:"//graph.facebook.com/fql?q=SELECT url, normalized_url, share_count, like_count, comment_count, total_count,commentsbox_count, comments_fbid, click_count FROM link_stat WHERE url=\""},twitter:{baseUrl:"//urls.api.twitter.com/1/urls/count.json?url="},pinterest_share:{baseUrl:"//widgets.pinterest.com/v1/urls/count.json?url="},pinterest:{baseUrl:"//widgets.pinterest.com/v1/urls/count.json?url="},reddit:{cb:function(G){var I=G.params,F=G.data,d=0,E=0,H=0,w;if(F.data&&F.data.children){w=F.data.children;for(var a=0;a<=w.length-1;a+=1){if(w[a].data&&w[a].data.downs!=null&&w[a].data.ups!=null){d+=w[a].data.ups;E+=w[a].data.downs;H+=w[a].data.score;}}G.callbackFunc({elem:I.elem,service:I.service,countUrl:I.countUrl,ups:+d,downs:+E,count:+H});}},baseUrl:"//www.reddit.com/api/info.json?url=",jsonpParam:"jsonp"},delicious:{cb:function(d){var w=d.params,a=d.data;d.callbackFunc({elem:w.elem,service:w.service,countUrl:w.countUrl,count:a.length?+a[0].total_posts:"0"});},baseUrl:"//feeds.delicious.com/v2/json/urlinfo/data?url="},vk:{ajs:function(a){var d=a.params;if(!window.VK){VK={Share:{count:function(){clearTimeout(a.timeout);var w=this.counts[arguments[0]];a.callbackFunc({elem:w.elem,service:w.service,countUrl:w.countUrl,count:+arguments[1]});}}};}VK.Share.counts=VK.Share.counts||[];VK.Share.counts.push(d);_ate.ajs(this.baseUrl+(VK.Share.counts.length-1)+"&url="+_euc(d.countUrl),1);},baseUrl:"//vk.com/share.php?act=count&index="},linkedin:{baseUrl:"//www.linkedin.com/countserv/count/share?url="},odnoklassniki_ru:{ajs:function(a){var d=a.params,w=a.cbname;_ate.ajs(this.baseUrl+_euc(d.countUrl)+"&"+this.jsonpParam+"="+w,1);},baseUrl:"//www.odnoklassniki.ru/dk?st.cmd=shareData&ref=",jsonpParam:"cb"},defaults:{cb:function(w){var E=w.params,d=w.data,a=+d.count;if(a!=null){w.callbackFunc({elem:E.elem,service:E.service,countUrl:E.countUrl,count:isNaN(a)?"0":a,error:isNaN(a)});}},ajs:function(a){var d=a.params,w=a.cbname;_ate.ajs(this.baseUrl+_euc(d.countUrl)+"&"+this.jsonpParam+"="+w,1);},jsonpParam:"callback"}},timeout:10000,getCounts:function(F,d){if(F.elem){F.elem.style.display="block";}if(!h||!h.services||!h.services.defaults){d({elem:F.elem,service:F.service,countUrl:F.countUrl,error:"Could not find necessary JavaScript object",count:"?"});return;}if(!h.services[F.service]||!h.services[F.service].baseUrl){d({elem:F.elem,service:F.service,countUrl:F.countUrl,error:"Service not supported",count:"?"});return;}var a=h.services[F.service],E=h.services.defaults,H=F.countUrl,w,G;a.jsonpParam=a.jsonpParam||E.jsonpParam||"callback";H=H.length>25?H.substring(0,25):H;w=setTimeout(function(){d({elem:F.elem,service:F.service,countUrl:F.countUrl,error:"Service request timed out",count:"?"});},h.timeout);G=_ate.util.scb("rcb",H,function(I){clearTimeout(w);if(a.cb){a.cb({params:F,data:I,callbackFunc:d});}else{if(E.cb){E.cb({params:F,data:I,callbackFunc:d});}}});if(F.service==="pinterest_share"||F.service==="pinterest"){G="window."+G;}if(a.ajs){a.ajs.call(a,{params:F,callbackFunc:d,cbname:G,timeout:w});}else{if(E.ajs){E.ajs.call(a,{params:F,callbackFunc:d,cbname:G});}}return this;}};var l={getShareCounts:function(E,F){if(!E){return;}var a=-1,w=E.services||E.service||E,d=E.url||E.countUrl;counturl=d||(p.addthis_share||{}).trackurl||_ate.track.mgu(({}).url||(p.addthis_share||{}).url,{clean:1,defrag:1}),promise=[];if(this.utils.isArray(w)){while(a<w.length-1){a+=1;h.getCounts({service:w[a],countUrl:counturl},function(G){promise.push(G);if(promise.length===w.length){F.call(this,promise);}});}}else{if(typeof w==="string"){h.getCounts({service:w,countUrl:counturl},function(G){F.call(this,G);});}}return this;},utils:{isArray:function(a){if("isArray"in Array){return Array.isArray(a);}else{return Object.prototype.toString.call(a)==="[object Array]";}}}};function k(I,E,K){if(I){I=_ate.util.select(I);for(var G=0;G<I.length;G++){var a=I[G],H=((a.parentNode||{}).className||"").indexOf("addthis_toolbox")>-1?addthis.util.getAttributes(a.parentNode,E,K):((((a.parentNode||{}).parentNode||{}).className||"").indexOf("addthis_toolbox")>-1?addthis.util.getAttributes(a.parentNode.parentNode,E,K):null),J=addthis.util.getAttributes(a,H?H.conf:E,H?H.share:K,true);if(!a.ost){if(a.className.indexOf("addthis_counter")==-1){a.className+=" addthis_counter";}if(_ate.bro.ie6&&a.className.indexOf("compatmode")==-1){a.className+=((a.className.indexOf("bubble_style")>-1)?" bubble":" ")+"compatmode"+_ate.bro.mod;}if(_ate.bro.ie6&&a.className.indexOf("ie6")==-1){a.className+=" ie6";}else{if(_ate.bro.ie7&&a.className.indexOf("ie7")==-1){a.className+=" ie7";}}a.url=(K||J.share||p.addthis_share||{}).trackurl||_ate.track.mgu((K||{}).url||J.share.url||(p.addthis_share||{}).url,{clean:1,defrag:1});a.addthis_conf=J.conf;a.addthis_share=J.share;a.ost=1;if(J.conf&&J.conf.service){var F=_ate.util.parent(a,".addthis_toolbox"),d=F.className!=null?F.className.indexOf("addthis_floating_style")!==-1:"",w=F.className!=null?F.className.indexOf("native-counter")!==-1:"";if(d&&!w){F.className+=" native-counter";}h.getCounts({elem:a,service:J.conf.service,countUrl:a.url},function(L){y(L.elem,m(L.count));});}else{z(a,function(L,M){c(L,M);});}}}}}function v(w,a,d){k(w,a,d);}function i(H,d,G){if(H){H=_ate.util.select(H);for(var w=0;w<H.length;w++){var F=H[w],E=((F.parentNode||{}).className||"").indexOf("addthis_toolbox")>-1?addthis.util.getAttributes(F.parentNode,d,G):null,a=addthis.util.getAttributes(F,E?E.conf:d,E?E.share:G,true);if(!F.ost){F.url=(G||a.share||p.addthis_share||{}).trackurl||_ate.track.mgu((G||{}).url||a.share.url||(p.addthis_share||{}).url,{clean:1,defrag:1});F.addthis_conf=a.conf;F.addthis_share=a.share;F.ost=1;b(F.url,function(I){F.innerHTML=I.error?"?":I.shares;});}}}}function f(){addthis.count=i;addthis.counter=v;addthis.sharecounters=l;addthis.data.getShareCount=function(d,a){if(!a){a=addthis_share;}b(typeof(a)=="string"?a:a.trackurl||a.url,d);};addthis.count.ost=1;addthis.counter.ost=1;addthis.sharecounters.ost=1;}if(_adr.isReady){f();return v;}else{addthis.addEventListener("addthis.ready",f);return addthis;}})();
