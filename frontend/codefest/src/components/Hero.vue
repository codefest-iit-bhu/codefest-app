<template>
	<header ref="header" :class="$style.hero">
		<!-- <Nav /> -->
		<div :class="$style.titles">
			<h1 ref="title">Codefest'19</h1>
		</div>
		<canvas ref="rains" :class="$style.rains" ></canvas>
	</header>
</template>

<script>
	import Nav from '@components/Nav';

	export default {
		components: {
			Nav
		},

		mounted() {
			const c = this.$refs.rains;
			var ctx = c.getContext("2d");
			c.height = window.innerHeight;
			c.width = 2*window.innerWidth;
			var code = "01";
			code = code.split("");
			var font_size = 35;
			var columns = 2*c.width/font_size;
			var drops = [];
			for(var x = 0; x < columns; x++) drops[x] = 1; 
			function draw(){
				ctx.fillStyle = "rgba(0, 0, 0, 0.03)";
				ctx.fillRect(0, 0, c.width, c.height);
				ctx.fillStyle = "#86ff00";
				ctx.font = font_size + "px arial";
				for(var i = 0; i < drops.length; i++){
					var text = code[Math.floor(Math.random()*code.length)];
					ctx.fillText(text, i*font_size, drops[i]*font_size);
					
					if(drops[i]*font_size > c.height && Math.random() > 0.975) drops[i] = 0;
					
					drops[i]++;
				}
			}

			setInterval(draw, 30);

		}
	}
</script>

<style module lang="styl">
	.hero
		position relative
		background-color var(--dark)
		border-bottom 2px solid var(--blue)
		max-height 600px
		min-height 300px
		height 45vh
	
	.rains
		height 100%
		width 100%
		position absolute
		overflow hidden
		bottom 0
		top 0
	
	.titles
		cursor pointer
		height 0
		z-index 2
		position relative
		font-family var(--font-header), var(--font-list)
		text-transform uppercase
		top calc(40% - 2px)
		text-align center
		h1
			font-size 2.875em
			font-weight 800
			line-height 1
			color var(--offwhite)
	
	.shape
		--size 30px
		position absolute
		will-change transform
		background transparent no-repeat center
		background-size contain
		height var(--size)
		width var(--size)
	
	:global(.penta)
		background-image url("@assets/shapes/penta.svg")
	
	:global(.point)
		background-image url("@assets/shapes/point.svg")
	
	:global(.square)
		background-image url("@assets/shapes/square.svg")
	
	:global(.cross)
		background-image url("@assets/shapes/cross.svg")
	
	:global(.circle)
		background-image url("@assets/shapes/circle.svg")
	
	@media screen and (max-width: 421px)
		.shape
			--size 20px
</style>
