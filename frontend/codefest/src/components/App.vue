<template>
	<div :class="$style.app">
        <router-view />
	</div>
</template>

<script>
	export default {
	}
</script>

<style module lang="styl">
	.app
		position relative
</style>
