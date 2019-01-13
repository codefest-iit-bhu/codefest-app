<template>
	<div :class="$style.app">
		<Hero />

		<main :class="$style.wrapper">
			<router-view />
		</main>

		<Footer />
	</div>
</template>

<script>
	import Footer from '@components/Footer';
	import Hero from '@components/Hero';

	export default {
	  components: {
	    Footer,
			Hero,
	  }
	}
</script>

<style module lang="styl">
	.app
		position relative
	
	.wrapper
		width 75%
		margin 0 auto
		position relative
		min-height calc(55vh - 16px)
		z-index 1
	
	@media screen and (max-width: 769px)
		.wrapper
			width 90%
</style>
