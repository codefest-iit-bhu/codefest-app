<template>
  <div :class="$style.lookback">
    <h1>LOOKBACK</h1>
    <div :class="$style.cell" v-for="(stat, i) in stats" :key="i">
      <div :class="$style.clip">
        <img :src="stat.image" :class="$style.img">
      </div>
      <div :class="$style.txt">
        {{ stat.name }}
        <br>
        {{ stat.value }}
      </div>
    </div>
    <br>

    <!-- <svg class="clip-svg">
			<defs>
				<clipPath id="hexagon-clip" clipPathUnits="objectBoundingBox">
					<polygon points="0.25 0.05, 0.75 0.05, 1 0.5, 0.75 0.95, 0.25 0.95, 0 0.5" />
				</clipPath>
			</defs>
    </svg>-->
  </div>
</template>
<script>
export default {
  data() {
    return {
      stats: [
        {
          name: "Prize Money",
          value: "500,000",
          image: "../assets/Lookback/25473.png"
        },
        {
          name: "Countries",
          value: "98",
          image: "../assets/Lookback/mobile-test-studio-locations-icon.png"
        },
        {
          name: "Participants",
          value: "24,654",
          image:
            "../assets/Lookback/kisspng-computer-icons-internet-forum-discussion-group-blo-5aff15db0bb4c8.818433001526666715048.png"
        },
        {
          name: "Unique Visitors",
          value: "328,902",
          image: "../assets/Lookback/visitor.png"
        },
        {
          name: "Registrations",
          value: "16,302",
          image: "../assets/Lookback/edit-user-male.png"
        }
      ]
    };
  }
};
</script>

<style module lang="styl">
	.lookback
		padding 24px
		background black
		border-radius var(--radius)
		box-shadow 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23)
		margin-bottom 32px
		font-family "Aldo the Apache"
		font-size 20px

		.cell
			width 500px
			height 100px
			margin-left auto
			margin-right auto

			.txt
				color #86ff00
				position relative
				top -70%

			.clip
				clip-path: polygon(25% 5%, 75% 5%, 100% 50%, 75% 95%, 25% 95%, 0% 50%);
				background white
				width 100px
				height 100px
				background #57a300

			.img
				width 80%
				height 80%
				position relative
				top -25%
				left 10%

			&:nth-child(2)
				.img
					top 0%
					left 0%
					width: 80%
					height: 80%
					margin: 10px

			&:nth-child(odd)
				.txt
					margin-right 55%
					text-align right
					float right
				
				.clip
					margin-left 50%

			&:nth-child(even)
				.txt
					margin-left 55%
					text-align left
					float left
				
				.clip
					margin-left 30%
	
		h1
			color #86ff00
			margin-bottom 16px
			text-align center
			padding 16px
</style>