(function(){function b(c,d,i,l,f,k,h,g){addthis_config={data_track_clickback:false,product:"ad-300"};function e(){icon_wrap=document.createElement("ul");icon_wrap.setAttribute("id","at_icon_wrap");icon_wrap.className+=i;icon_wrap.className+=" "+l;icon_wrap.className+=f=="square"?" square":" rectangle";for(var m in k){li=document.createElement("li");a=document.createElement("a");a.setAttribute("target","_blank");a.setAttribute("addthis:userid",k[m]);if(m=="linkedin_company"){li.className="linkedin";a.setAttribute("addthis:usertype","company");a.className="addthis_button_linkedin_follow";}else{if(m=="linkedin_group"){li.className="linkedin";a.setAttribute("addthis:usertype","group");a.className="addthis_button_linkedin_follow";}else{li.className=m;a.className=(m=="share")?"addthis_button_share":"addthis_button_"+m+"_follow";}}icon=document.createElement("span");icon.className=m;a.appendChild(icon);li.appendChild(a);icon_wrap.appendChild(li);}return icon_wrap;}function j(){wrap=document.getElementById(c);dim=d.split("x");wh="width:"+dim[0]+"px; height:"+dim[1]+"px;";wrap.style.cssText=wh;wrap.id="embed_wrapper";wrap.appendChild(e());if(k.share!=undefined){if(typeof g!=undefined){addthis.toolbox(wrap,addthis_config,{url:k.share,title:g});}else{addthis.toolbox(wrap,addthis_config,{url:k.share});}}else{addthis.toolbox(wrap);}}j();}addthis.ad=addthis.ad||{};_ate.extend(addthis.ad,{embed:{ost:1},menu:b});})();