<template>

	<div id="hero" class="preload" :class="$style.hero">
		<mq-layout mq="lg+">
		<canvas id="canvas" v-if="themeisdark" ref="rains" :class="$style.anim" :style="{ backgroundImage: 'url(' + require('@/assets/hero/background-dark.jpg') + ')' }"></canvas>
		<canvas id="canvas" v-else ref="rains" :class="$style.anim" :style="{ backgroundImage: 'url(' + require('@/assets/hero/background.jpg') + ')' }"></canvas>
		<div id="title" class="absolute-center1" :class="$style.title">
	        <div :class="$style.cftitle">
	          <span>
	            <img v-if="themeisdark" :class="$style.mainlogo" src="@assets/hero/logo-dark.png">
	            <img v-else :class="$style.mainlogo" src="@assets/hero/logo.png">
	          </span>
	          <!--<h1 :class="$style.heroTitle">
		        code
		        <span>Fest</span>
		        <sup>20</sup>
		        </h1>-->
	          <span id="tagline" :class="$style.tagline">Imagine. Create. Iterate.</span>
	          
	        </div>
      	</div>
      	<div :class="$style.wrap">
      		<img v-if="themeisdark" :class="$style.wrapimg" src="@assets/hero/hero-wrap-dark.svg">
      		<img v-else :class="$style.wrapimg" src="@assets/hero/hero-wrap.svg">
      	</div>
		</mq-layout>
		<mq-layout :mq="['sm', 'xs', 'md']">
	      <div class="absolute-center" :class="[$style.smallhero, $style[$mq]]">
	        <div :class="$style.cflogo">
	          <svg viewBox="0 0 335.71 293.38">
	            <path
	              class="cls-1"
	              d="M170.18,293.38V49.4c-1.81-.58-119.63-.82-124.31-.3-.51,1.78-.76,142.54-.23,148.75,5.27.28,10.59.09,15.9.12s10.72,0,16.08,0h65c-7.7,16.54-15.36,32.66-22.92,48.77H0V.44C.08.36.13.3.19.25S.31.12.38.11A6,6,0,0,1,1.32,0Q168.24,0,335.15,0c.13,0,.26.13.56.3a12.17,12.17,0,0,1-1,1.23Q311.86,24.64,289,47.75a4.24,4.24,0,0,1-3.44,1.19H215.78c-.52,1.91-.7,45.89-.23,50.23,2.79.27,5.64.09,8.48.12s5.92,0,8.88,0h52.44c-.8.91-1.23,1.45-1.71,1.94q-21.66,21.94-43.3,43.92a5,5,0,0,1-4,1.62c-6-.09-12,0-18,0h-2.94c0,1.15,0,2.15,0,3.16q0,46.56,0,93.11a15.68,15.68,0,0,0,0,1.68,4.34,4.34,0,0,1-1.49,3.8Q194.9,268,176,287.64C174.23,289.47,172.38,291.21,170.18,293.38Z"
	            ></path>
	          </svg>
	        </div>
	        <div :class="$style.cftext">
	          <span :class="$style.smalltagline" ref="tagline"></span>
	          <!--<p :class="$style.loc">
	            <i class="fas fa-map-marked-alt"></i> IIT (BHU), Varanasi
	          </p>-->
	        </div>
	        <div :class="$style.registerbtn">
	          <router-link to="/login">
	            <span :class="$style.register">Register</span>
	          </router-link>
	        </div>
	      </div>
	    </mq-layout>
	</div>
</template>

<script>
import { TypingAnim } from "@js/utils";

export default {

  computed: {

  	themeisdark: function() {

        if( this.$store.getters.currentTheme == 'dark')	return true;
        return false;
    }
  },
  methods: {
    initMatrixRain() {

		const canvas = this.$refs.rains;

		var ctx = canvas.getContext("2d");

		var wid = window.innerWidth;
		var heig = window.innerHeight;

		canvas.width = wid;
		canvas.height = heig;

		const foot = [

		    [241,6,227,-27,193,-54,166,-71,126,-81,93,-87,60,-88,22,-86,-14,-79,-37,-69,-49,-53,-53,-21,-60,23,-64,65,-45,88,-15,95,16,97,70,100,114,97,150,90,189,72,223,44],
		    [-123,6,-117,-30,-114,-62,-140,-70,-168,-74,-201,-76,-230,-60,-251,-27,-253,12,-244,41,-217,57,-176,62,-135,64,-129,42]
		]																			// shape of left footstep
		const footScale = 0.03; 													// size of footstep
		const fadeRate = 0.65;														// change rate of fading of footsteps
		const stepLen = 24; 														// change length of step taken by single foot
		var stepCount = 0; 
		var stepCount1 = 0;
		var stepCount2 = 0;
		var stepCount3 = 0;
		var stepTime = Math.random()*(300) + 400;							// time taken(in ms) to move 1 step, random value between [300,600]

		var path = [250,946,172,592,186,270,90,206,170,38];										// set of len/2 vertices with tell the path followed by footsteps
		var path1 = [522,670,970,520,904,192,398,192,284,192,374,219];
		var path2 = [1622,94,1498,88,1512,50,1616,52,1614,180,1768,184];
		var path3 = [1720,974,1400,676,1144,562,1140,409,1820,404];

		var wscale = wid/1920;


		var pLen = path.length;														// scale the path as per window co-ordinates
		var pLen1 = path1.length;
		var pLen2 = path2.length;
		var pLen3 = path3.length;
		var i;

		for(i=0;i < pLen; i++)	path[i] = (path[i]*wscale);
		for(i=0;i < pLen1; i++)	path1[i] = (path1[i]*wscale);
		for(i=0;i < pLen2; i++)	path2[i] = (path2[i]*wscale);
		for(i=0;i < pLen3; i++)	path3[i] = (path3[i]*wscale);

		for(i=pLen-2; i > -1 ;i-=2){

		    path.push(path[i]);
		    path.push(path[i+1]);
		}

		for(i=pLen1-2; i > -1 ;i-=2){

		    path1.push(path1[i]);
		    path1.push(path1[i+1]);
		}

		for(i=pLen2-2; i > -1 ;i-=2){

		    path2.push(path2[i]);
		    path2.push(path2[i+1]);
		}

		for(i=pLen3-2; i > -1 ;i-=2){

		    path3.push(path3[i]);
		    path3.push(path3[i+1]);
		}

		pLen = path.length;
		pLen1 = path1.length;
		pLen2 = path2.length;
		pLen3 = path3.length;

		var pos = {
		    x : path[0],
		    y : path[1],
		    index : 0,
		};

		var pos1 = {
		    x : path[0],
		    y : path[1],
		    index : 0,
		};

		var pos2 = {
		    x : path1[0],
		    y : path1[1],
		    index : 0,
		};

		var pos3 = {
		    x : path1[0],
		    y : path1[1],
		    index : 0,
		};

		var pos4 = {
		    x : path2[0],
		    y : path2[1],
		    index : 0,
		};

		var pos5 = {
		    x : path2[0],
		    y : path2[1],
		    index : 0,
		};

		var pos6 = {
		    x : path3[0],
		    y : path3[1],
		    index : 0,
		};

		var pos7 = {
		    x : path3[0],
		    y : path3[1],
		    index : 0,
		};

		function getnextStep(dist,pos){														// get the next position of footstep if it is currently at pos

		    var nx = path[(pos.index + 2) % pLen] - pos.x;									// difference in x,y between pos and next point in path
		    var ny = path[(pos.index + 3) % pLen] - pos.y;
		    var d = Math.hypot(nx, ny);
		    if(d > dist){
		        pos.x += (nx / d) * dist;
		        pos.y += (ny / d) * dist;
		        return pos;
		    }

		    dist -= d;
		    pos.index += 2;
		    pos.x = path[pos.index % pLen];
		    pos.y = path[(pos.index + 1) % pLen];

		    return getnextStep(dist, pos);
		}

		function getnextStep1(dist,pos2){

		    var nx = path1[(pos2.index + 2) % pLen1] - pos2.x;
		    var ny = path1[(pos2.index + 3) % pLen1] - pos2.y;
		    var d = Math.hypot(nx, ny);
		    if(d > dist){
		        pos2.x += (nx / d) * dist;
		        pos2.y += (ny / d) * dist;
		        return pos2;
		    }

		    dist -= d;
		    pos2.index += 2;
		    pos2.x = path1[pos2.index % pLen1];
		    pos2.y = path1[(pos2.index + 1) % pLen1];

		    return getnextStep1(dist, pos2);
		}

		function getnextStep2(dist,pos4){

		    var nx = path2[(pos4.index + 2) % pLen2] - pos4.x;
		    var ny = path2[(pos4.index + 3) % pLen2] - pos4.y;
		    var d = Math.hypot(nx, ny);
		    if(d > dist){
		        pos4.x += (nx / d) * dist;
		        pos4.y += (ny / d) * dist;
		        return pos4;
		    }

		    dist -= d;
		    pos4.index += 2;
		    pos4.x = path2[pos4.index % pLen2];
		    pos4.y = path2[(pos4.index + 1) % pLen2];

		    return getnextStep2(dist, pos4);
		}

		function getnextStep3(dist,pos6){

		    var nx = path3[(pos6.index + 2) % pLen3] - pos6.x;
		    var ny = path3[(pos6.index + 3) % pLen3] - pos6.y;
		    var d = Math.hypot(nx, ny);
		    if(d > dist){
		        pos6.x += (nx / d) * dist;
		        pos6.y += (ny / d) * dist;
		        return pos6;
		    }

		    dist -= d;
		    pos6.index += 2;
		    pos6.x = path3[pos6.index % pLen3];
		    pos6.y = path3[(pos6.index + 1) % pLen3];

		    return getnextStep3(dist, pos6);
		}

		function drawFoot(x,y,dir,left){														// draw the footstep on canvas as per position, mirror and angle

		    var i,j,shape;
		    var xdx = Math.cos(dir) * footScale;
		    var xdy = Math.sin(dir) * footScale;
		    
		    if(left){

		        ctx.setTransform(xdx, xdy, -xdy, xdx, x + xdy * 50, y - xdx * 50);
		        ctx.rotate(-0.1);
		    }
		    else{
		        ctx.setTransform(xdx, xdy, -xdy, xdx, x - xdy * 50, y + xdx * 50);
		        ctx.rotate(-0.1);
		        ctx.scale(1,-1);
		    }

		    ctx.beginPath();
		    for(j = 0; j < foot.length; j ++){
		        shape = foot[j];
		        i = 0;
		        ctx.moveTo(shape[i++],shape[i++]);
		        while(i < shape.length){
		            ctx.lineTo(shape[i++],shape[i++]);
		        }
		        ctx.closePath();
		    }
		    ctx.fill();
		}

		ctx.setTransform(1,0,0,1,0,0);
		ctx.clearRect(0,0,canvas.width,canvas.height);
		pos1 = getnextStep(stepLen/10,pos1);
		pos3 = getnextStep1(stepLen/10,pos3);
		pos5 = getnextStep2(stepLen/10,pos5);
		pos7 = getnextStep3(stepLen/10,pos7);
		var globalthis = this;

		function Fade(){																	// implements the Fade effect

		    let imageData = ctx.getImageData(0,0,canvas.width,canvas.height);
		    let data = imageData.data;

		    for (var i=0; i < data.length; i+=4) {

		        data[i+3] = fadeRate*data[i+3];
		    }

		    ctx.putImageData(imageData,0,0);
		}

		function setpage(){

			document.getElementById("title").style.display = "block";
			document.getElementById("tagline").style.animation = "var(--hero-text-animation)";

		}

		function draw(){																	// main

		    pos = getnextStep(stepLen,pos);
		    pos1 = getnextStep(stepLen,pos1);
		    pos2 = getnextStep1(stepLen,pos2);
		    pos3 = getnextStep1(stepLen,pos3);
		    pos4 = getnextStep2(stepLen,pos4);
		    pos5 = getnextStep2(stepLen,pos5);
		    pos6 = getnextStep3(stepLen,pos6);
		    pos7 = getnextStep3(stepLen,pos7);
		    var dark = globalthis.themeisdark ;
		    if(dark)    ctx.fillStyle = "rgba(255, 255, 255, 1)";
		    else ctx.fillStyle = "rgba(0, 0, 0, 1)";
		    
		    drawFoot(pos.x,pos.y,Math.atan2(pos1.y - pos.y, pos1.x - pos.x),(stepCount++) % 2 === 0);	// send co-ordinates, angle of inclination and (left/right) foot
		    if(!dark)	drawFoot(pos2.x,pos2.y,Math.atan2(pos3.y - pos2.y, pos3.x - pos2.x),(stepCount1++) % 2 === 0);
		    drawFoot(pos4.x,pos4.y,Math.atan2(pos5.y - pos4.y, pos5.x - pos4.x),(stepCount2++) % 2 === 0);
		    if(!dark)	drawFoot(pos6.x,pos6.y,Math.atan2(pos7.y - pos6.y, pos7.x - pos6.x),(stepCount3++) % 2 === 0);
		    Fade();
		    setTimeout(draw,stepTime);
		}

		function BackgroundLoader() {

		  var url;
		  var dark = globalthis.themeisdark ;
		  if(dark)	url = require('@/assets/hero/background-dark.jpg');
		  else url = require('@/assets/hero/background.jpg');
		  var loaded = false;
		  var image = new Image();

		  image.onload = function () {
		    loaded = true;
		    var div = document.getElementById("canvas");
		    div.style.backgroundImage = "url('" + url + "')";
		  }
		  image.src = url;      

		  setTimeout(function() {
		    if (loaded){
		      setpage();
		      draw();
		      }

		  }, 1000);

		}
		BackgroundLoader();
		
    	
    },
    tryMatrixRain() {
      if (["lg", "xl", "xxl"].includes(this.$mq)) {

      	this.initMatrixRain();
        
      }
    }
  },
  mounted() {
    this.tryMatrixRain();
    if (!["lg", "xl", "xxl"].includes(this.$mq)){

	    this.animTyping = new TypingAnim(
	      this.$refs.tagline,
	      "Imagine. Create. Iterate."
	    );

	    window.setInterval(() => {
	      this.isTyped ? this.animTyping.erase() : this.animTyping.type();
	      this.isTyped = !this.isTyped;
	    }, 2000);
	    this.animTyping.type();
	    this.isTyped = true;
	}

  },
  watch: {
    $mq: function() {
      setTimeout(this.tryMatrixRain.bind(this), 500);
    }
  }
};
</script>

<style module lang="stylus">
@require '~@styles/theme';
@require '~@styles/anims';

.preload * {

  -webkit-transition: none !important;
  -webkit-animation: none !important;
  -moz-transition: none !important;
  -ms-transition: none !important;
  -o-transition: none !important;
}

.anim {
  height: 100%;
  width: 100%;
  position: absolute;
  overflow: hidden;
  bottom: 0;
  top: 0;
  background-size: 100%;
}

.hero{
	
	position: relative;
	min-height: 300px;
	height: 100vh;
	max-width: 100%;
	overflow: hidden;
	color: #f1f1f1;

}

.wrap{
	
	position: absolute;
	width: 100vw;
	z-index: 2;
	min-height: 1px;
	bottom: -2vh;

	.wrapimg{

		bottom: 0vh;
		width: 100vw;
	}
}

.title {

  display: none;
  height: 30%;
  width: 100%;
  z-index: 2;
  margin: auto;
  text-align: center;

  .cftitle {
    width: 60%;
    margin-left: 20%;
    padding-right: 5%;
    padding-left: 5%;
    padding-top: 50px;
    padding-bottom: 50px;
    border-radius: 300px;
    backdrop-filter: blur(0.01em);

    .mainlogo{

    	width: 40vw;
    }

    .heroTitle{

      font: 100px 'Harry';
      font-weight: 600;
      text-align: center;
      color: var(--hero-text-color);
    }

    .tagline {
      display: block;
      margin: 10px auto;
      height: 32px;
      font: 26px 'Harry';
      font-weight: 600;
      text-align: center;
      text-shadow: 1px 1px #000;
      color: var(--hero-text-color);
      letter-spacing: 3px;
    }

    ~/.xs .tagline, ~/.sm .tagline {
      font-size: 20px;
    }

    .venue {
      font-size: 22px;

      #loc, #date {
        display: inline-block;
        padding: 4px;
      }

      #loc::after {
        // content: '|';
        // margin-left: 2px;

        ~/.xs ^[1..-1] {
          content: '';
          margin: unset;
        }
      }

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        font-size: 16px;
      }
    }
  }
}

.roundbox{
	
	position: absolute;
	border-radius: 25px;
	padding: 20px; 
	width: 50%;
	max-width: 60%;
	min-height: 250px;
	max-height: 300px;
	border-width: 2px;
	margin-left:20%;
	margin-top: 15%;
}

.smallhero {

  color: $orange;

  .aws {
    margin: auto;
    height: 100px;
    width: 100px;
    border-radius: 50px;
    padding: 10px;
    background: $white;

    img {
      width: 100%;
    }
  }

  .presents {
    margin: 15px auto;
    font-family: 'Ubuntu';
    font-weight: 600;
    color: $white;
    text-align: center;
  }

  .cflogo {
    width: 100%;
    margin: auto;

    svg {
      width: 350px;
      height: 300px;
      display: inline-block;

      path {
        fill: $chartreuse;
        animation: svg-transform 2.5s ease-in-out infinite alternate;
      }

      ~/.sm ^[1..-1] {
        width: 280px;
        height: 240px;
      }

      ~/.xs ^[1..-1] {
        width: 210px;
        height: 180px;
      }
    }
  }

  .cftext {
    width: 100%;
    display: block;
    padding-top: 50px;

    .smalltagline {
      display: block;
      margin: 10px auto;
      height: 32px;
      font: 26px 'Ubuntu';
      text-align: center;

      ~/.xs ^[1..-1], ~/.sm ^[1..-1] {
        font-size: 16px;
      }
    }

    ~/.sm ^[1..-1] {
      font-size: 16px;
    }

    ~/.xs ^[1..-1] {
      font-size: 16px;
    }

    p {
      margin-bottom: 10px;
      font-family: 'Roboto Slab';
      font-weight: 600;
      text-align: center;

      ~/.md ^[1..-1] {
        margin: 0;
        display: inline-block;
      }
    }
  }

  ./md ^[1..-1] {
    padding-top: 150px;
  }
}

.registerbtn {
  text-align: center;
  padding-top: 20px;

  .register {
    margin: auto;
    margin-top: 10px;
    margin-bottom: 10px;
    height: auto;
    padding: 10px 20px;
    border-radius: 50px;
    border: 2px solid $darkorange;
    text-align: center;
    cursor: pointer;
    color: $orange;
    font-family: 'Roboto Slab';
    font-weight: 600;
    box-shadow: inset 0px 0px 10px $orange;
  }
}

</style>