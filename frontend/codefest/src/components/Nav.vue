<template>
	<nav :class="[$style.nav, { [$style.stuck]: stuck }]">
		<ul :class="$style.links">
			<li><router-link to="/">Home</router-link></li>
			<li><router-link to="/blog">Blog</router-link></li>
			<li><router-link to="/about">About</router-link></li>
		</ul>

		<ul>
			<li><a href="https://github.com/lukeed/pwa" :class="$style.link_external">GitHub</a></li>
			<li><a href="https://github.com/lukeed/pwa" :class="$style.link_external">Documentation</a></li>
		</ul>
	</nav>
</template>

<script>
	export default {
		data() {
			return {
				stuck: false
			};
		},
		mounted() {
			addEventListener('scroll', ev => {
				this.stuck = window.pageYOffset > 0;
			}, { passive:true });
		}
	}
</script>

<style module lang="styl">
	.nav
		width 100%
		height 56px
		display flex
		padding 0 32px
		position relative
		background transparent
		justify-content space-between
		align-items center
		position sticky
		z-index 9
		top 0
		&::after
			opacity 0
			content ''
			transition opacity var(--transition-duration)
			box-shadow 0 3px 6px rgba(0,0,0, 0.16), 0 3px 6px rgba(0,0,0, 0.23)
			background var(--offwhite)
			will-change opacity
			position absolute
			height 100%
			width 100%
			left 0
			top 0
		li
			display inline-block
			position relative
			margin-left 24px
			list-style none
			float right
			z-index 1
	
	.stuck
		&::after
			opacity 1
	
	.logo
		height 24px
		z-index 1
	
	.link_external
		position relative
		padding-right 8px
		&::after
			content ''
			position absolute
			background transparent no-repeat center
			background-image url("@assets/link.svg")
			height 12px
			width 12px
			right -8px
	
	.links li
		float none
		margin-left 0
		margin-right 24px
	
	@media screen and (max-width: 421px)
		.nav
			font-size 75%
			padding 0 16px
			li
				margin-left 16px
		.links li
			margin-left 0
			margin-right 16px
</style>
