<template>
  <div :id="$style.events">
    <h1 :class="$style.title">Events</h1>
    <div :class="$style.cell" @mouseenter="glitch(event.name, event.image, 1)" @mouseleave="glitch(event.name, event.image, -1)" v-for="(event, i) in events" :key="i">
        <canvas :id="'canvas_'+ event.name + '_normal'" :class="$style.normal_canvas" />
        <canvas :id="'canvas_'+ event.name + '_glitched'" :class="$style.glitched_canvas" />
        <div :class="$style.txt">
          {{ event.name }}
          <br>
          <div :class="$style.info">
            {{ event.value }}
          </div>
        </div>
    </div>
    <br>
  </div>
</template>
<script>
import { getRandom } from "../js/utils";

export default {
  data() {
    return {
      events: [
        {
          name: "Appathon",
          value: "A challenge to blend your creativity to develop a robust mobile app.",
          image: "../assets/events/appathon.png"
        },
        {
          name: "Enigma",
          value: "Solve real-life problems by letting your machine learn patterns.",
          image: "../assets/events/enigma.png"
        },
        {
          name: "Manthan",
          value: "Dive deep in the world of data structures and algorithms.",
          image:
            "../assets/events/manthan.png"
        },
        {
          name: "Vista",
          value: "Make machines perceive and hone your skills in Computer Vision.",
          image: "../assets/events/vista.png"
        },
        {
          name: "Perplexed",
          value: "Adapt to challenging situations by delving in constrained programming.",
          image: "../assets/events/perplexed.png"
        }
      ]
    };
  },
  methods: {
      glitch(id, image, type) {
        var requestAnimationFrame = window.requestAnimationFrame;
        
        var canvas_normal = document.getElementById('canvas_'+id+'_normal');

        var canvas_glitched = document.getElementById('canvas_'+id+'_glitched');


        var img = new Image();
        img.src = image;

        canvas_normal.setAttribute("width", img.width);
        canvas_normal.setAttribute("height", img.height);

        canvas_glitched.setAttribute("width", img.width);
        canvas_glitched.setAttribute("height", img.height);

        var verticalSlices = Math.round(img.height / 20);
        var maxHorizOffset = 20;

        var context_normal = canvas_normal.getContext('2d');
        var context_glitched = canvas_glitched.getContext('2d');

        var animate = function(canvas, duration, type) {
          var start = new Date().getTime();

          var step = function() {
            var timestamp = new Date().getTime();
            var progress = Math.min((timestamp - start) / duration, 1);
            canvas.style.opacity = (type > 0) ? progress : (1 - progress);

            var context = canvas.getContext('2d');
            context.clearRect(0, 0, canvas.width, canvas.height);

            for (var i = 0; i < verticalSlices; i++)  {
              var horizOffset = getRandom(-Math.abs(maxHorizOffset), maxHorizOffset);
              context.drawImage(img, 0, i * verticalSlices, img.width, i * verticalSlices + verticalSlices, horizOffset, i * verticalSlices, img.width, i * verticalSlices + verticalSlices);
            }

            if (progress < 1) requestAnimationFrame(step);
          };
          return step();
      };

      animate(canvas_normal, 1000, -type);
      animate(canvas_glitched, 1000, type);

      context_normal.drawImage(img, 0, 0);
      context_glitched.drawImage(img, 0, 0);

    }
  },

  mounted() {
      function draw(id, img) {
        var canvas = document.getElementById(id);
        var context = canvas.getContext('2d');
        canvas.setAttribute("width", img.width);
        canvas.setAttribute("height", img.height);
        context.drawImage(img, 0, 0);
      }

      this.events.forEach(function(event) {
          var img = new Image()
          img.src = event.image
          img.onload = function() {
            draw('canvas_'+event.name+'_normal', this);
          };
      }); 
  }
};


</script>

<style module lang="styl">

@import '../styles/theme.styl';
@import '../styles/anims.styl';


.title 
  padding 25px
  font-family "Aldo the Apache";
  font-size 56px;

#events
  min-height 1400px
  background #57a300

  .cell

    box-shadow 0 15px 20px rgba(0, 0, 0, 0.3)

    border-radius 100%
    width 55%
    height 150px
    margin 0 0 100px 0
    padding 0 20px
    background #86ff00
    cursor pointer

    &:hover
      width 60%
      transition all 0.1s ease-out

      .info
        display block
        animation typing 2s steps(40, end), blink-caret .75s step-end infinite
  
    &:nth-child(odd)
      float left
      border-radius 0 76px 76px 0
      .normal_canvas, .glitched_canvas
        float right
      .glitched_canvas
        position relative
        left 80%
        top 0
      .txt
        text-align left
      

    &:nth-child(even)
      float right
      border-radius 76px 0 0 76px
      .normal_canvas, .glitched_canvas
        float left
      .glitched_canvas
        position relative
        right 80%
        top 0
      .txt
        text-align right

    .txt
      font-family "Aldo the Apache"
      font-size 50px
      color #555
      text-transform uppercase
      margin 25px

    .info
      font-family monospace
      font-size 12px
      line-height 12px
      padding 2px 10px
      display none
      margin 2px auto
      text-align justify
      color #57a330
      overflow hidden
      border-right .15em solid orange
      letter-spacing .1em
      white-space: nowrap

    .normal_canvas, .glitched_canvas
      width 150px
      height 150px
      padding 25px
    
    .glitched_canvas
      opacity: 0;
        
</style>