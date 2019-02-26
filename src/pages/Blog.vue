<template>
	<div :class="$style.blog">
		<Intro>
			<h1>Welcome to my Blog!</h1>
			<p><span :class="$style.callout">NEW</span> articles posted every week. Please be sure to subscribe if you like what you see. 👀 Yadda yadda...</p>
			<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ea nam, ratione natus. Aliquid veritatis illo veniam. Quam tempora quia provident facilis, molestiae iure reiciendis officia, fugit vitae ullam voluptatem quis.</p>
			<p :class="$style.indent">Please select an Article to read:</p>
		</Intro>

		<div :class="$style.blog_grid">
			<router-link
				v-for="(_, idx) in items"
				:key="idx" :to="`/blog/article${idx}`"
				:class="$style.blog_item"
			>
				<Card>
					<strong v-html="'Article #' + idx" />
					<em>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Labore enim, natus. Beatae ducimus quasi doloremque ad quam qui dolor, architecto repellendus provident rem nostrum accusamus, magnam voluptate vel voluptas iste.</em>
				</Card>
			</router-link>
		</div>
	</div>
</template>

<script>
	import Intro from '@components/Intro';
	import Card from '@components/Card';

	export default {
		components: {
			Intro,
			Card
		},

		data() {
			return {
				items: Array.from({ length:10 })
			};
		}
	}
</script>

<style module lang="styl">
	.blog
		margin-top -64px
	
	.indent
		opacity 0.85
		font-style italic
		border-left 4px solid var(--blue)
		padding 4px 16px
	
	.blog_grid
		display grid
		grid-gap 16px
		grid-template-columns repeat(auto-fit, minmax(300px, 1fr))
		margin-bottom 32px
	
	.blog_item
		cursor pointer
		&:hover
			text-decoration none
		strong
			display block
			margin-bottom 8px
		em
			font-size 85%
			line-height 1
	
	.callout
		box-shadow: none
		font-weight: 800
		text-transform: uppercase
		font-family: var(--font-header)
		text-shadow: 2px 2px 0 rgb(255,210,23), 4px 4px 0 rgb(90,199,255)
		padding-right: 4px
</style>
