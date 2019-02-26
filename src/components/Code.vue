<template>
	<pre :class="[$style.pre, { [$style.offset]: offset }]">
		<span v-if="label" :class="$style.comment" v-html="'# '+ label" />
		<span :class="$style.text" v-html="'$ ' + text" />
	</pre>
</template>

<script>
	export default {
		props: ['offset', 'label', 'text']
	}
</script>

<style module lang="styl">
	.pre
		padding 12px
		background rgb(246, 248, 255)
		font-family 'Roboto Mono', monospace
		white-space initial
		line-height 1.5
		font-size 14px
	
	.offset
		margin-top -24px
	
	.comment
		display block
		color rgb(89, 89, 121)
	
	.text
		display block
		color rgb(16, 96, 182)
</style>
