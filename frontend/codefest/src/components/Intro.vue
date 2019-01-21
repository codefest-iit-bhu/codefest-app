<template>
	<div :class="$style.intro">
		<h1>A Byte About Us</h1>
		<p>	The Department of Computer Science and Engineering, IIT (BHU) Varanasi 
			brings to you yet another edition of its annual coding extravaganza, Codefest!
			Being more diverse than ever, Codefest '18 boasts of a plethora of events, 
			ranging from competitive programming, algorithms and application development 
			to upcoming trends like cryptography, machine learning, computer vision and cyber security.
			With problems being of varying difficulty levels, Codefest provides the perfect platform 
			for fresh enthusiasts, as well as the experienced ones, to code together and compete for ultimate glory.</p>
	</div>
</template>

<script>
	export default {
		//
	}
</script>

<style module lang="styl">
	.intro
		padding 24px
		background black
		border-radius var(--radius)
		box-shadow 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23)
		margin-bottom 32px
		font-family "Aldo the Apache"
		font-size 20px
	
		h1
			color #86ff00
			margin-bottom 16px
			text-align center
			padding 16px
	
		p
			margin-bottom 12px
			line-height 1.35
			color #86ff00
			&:last-of-type
				margin-bottom 0
</style>
