<template>
	<div :class="$style.features">
		<div :class="$style.item"
			v-for="item in items"
			:key="item.title"
		>
			<h3 v-html="item.title" />
			<p v-html="item.text" />
		</div>
	</div>
</template>

<script>
	import items from '@assets/features.json';

	export default {
		data() {
			return { items };
		}
	}
</script>

<style module lang="styl">
	.features
		display grid
		grid-gap 32px
		grid-template-columns repeat(auto-fit, minmax(260px, 1fr))
		padding-bottom 64px
	
	.item
		h3
			margin-bottom 8px
	
	@media screen and (min-width: 1200px)
		.features
			grid-template-columns repeat(3, 1fr)
</style>
