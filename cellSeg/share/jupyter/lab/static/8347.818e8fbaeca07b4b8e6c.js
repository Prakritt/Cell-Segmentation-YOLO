"use strict";(self["webpackChunk_jupyterlab_application_top"]=self["webpackChunk_jupyterlab_application_top"]||[]).push([[8347],{38347:(e,t,n)=>{n.r(t);n.d(t,{brainfuck:()=>r});var i="><+-.,[]".split("");const r={startState:function(){return{commentLine:false,left:0,right:0,commentLoop:false}},token:function(e,t){if(e.eatSpace())return null;if(e.sol()){t.commentLine=false}var n=e.next().toString();if(i.indexOf(n)!==-1){if(t.commentLine===true){if(e.eol()){t.commentLine=false}return"comment"}if(n==="]"||n==="["){if(n==="["){t.left++}else{t.right++}return"bracket"}else if(n==="+"||n==="-"){return"keyword"}else if(n==="<"||n===">"){return"atom"}else if(n==="."||n===","){return"def"}}else{t.commentLine=true;if(e.eol()){t.commentLine=false}return"comment"}if(e.eol()){t.commentLine=false}}}}}]);
//# sourceMappingURL=8347.818e8fbaeca07b4b8e6c.js.map?v=818e8fbaeca07b4b8e6c