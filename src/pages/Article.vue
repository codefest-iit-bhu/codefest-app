<template>
	<article :class="$style.article">
		<Intro>
			<h1 :class="$style.title" v-html="$route.params.title" />
			<span :class="$style.subtitle">A killer story</span>
			<p :class="$style.summary">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Doloribus laborum eaque sapiente dolorem nisi voluptate explicabo corporis, veritatis vero. Quae voluptates voluptatum ut quis quia alias tenetur impedit quam quaerat.</p>

			<div :class="$style.content">
				<router-link to="/blog" :class="$style.back">Back to Blog</router-link>
				<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam maiores necessitatibus nihil quo, cupiditate consectetur voluptatem cumque ipsum consequuntur aut repellat repellendus eligendi, placeat inventore perspiciatis dolores ipsa voluptates porro.</p>
				<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam maiores necessitatibus nihil quo, cupiditate consectetur voluptatem cumque ipsum consequuntur aut repellat repellendus eligendi, placeat inventore perspiciatis dolores ipsa voluptates porro.</p>
				<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam maiores necessitatibus nihil quo, cupiditate consectetur voluptatem cumque ipsum consequuntur aut repellat repellendus eligendi, placeat inventore perspiciatis dolores ipsa voluptates porro.</p>
				<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam maiores necessitatibus nihil quo, cupiditate consectetur voluptatem cumque ipsum consequuntur aut repellat repellendus eligendi, placeat inventore perspiciatis dolores ipsa voluptates porro.</p>
				<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam maiores necessitatibus nihil quo, cupiditate consectetur voluptatem cumque ipsum consequuntur aut repellat repellendus eligendi, placeat inventore perspiciatis dolores ipsa voluptates porro.</p>
				<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam maiores necessitatibus nihil quo, cupiditate consectetur voluptatem cumque ipsum consequuntur aut repellat repellendus eligendi, placeat inventore perspiciatis dolores ipsa voluptates porro.</p>
			</div>
		</Intro>

	</article>
</template>

<script>
	import Intro from '@components/Intro';

	export default {
		components: {
			Intro
		}
	}
</script>

<style module lang="styl">
	.article
		margin-top -64px
	
	.title
		text-transform capitalize
	
	.subtitle
		opacity 0.65
		display block
		text-indent 16px
		font-style italic
		margin-top -12px
	
	.summary
		padding-top 16px
	
	.content
		position relative
		border-top 2px solid var(--blue)
		padding-top 32px
		margin-top 32px
	
	.back
		top -16px
		display block
		padding 4px 12px
		position absolute
		margin-bottom 16px
		background var(--blue)
		border-radius var(--radius)
		font-family var(--font-header)
		text-transform uppercase
		color var(--offwhite)
		padding-left 32px
		line-height 20px
		font-weight 800
		font-size 80%
		&::after
			content '➤'
			position absolute
			transform rotate(180deg)
			font-size 14px
			left 10px
			top 4px
</style>
