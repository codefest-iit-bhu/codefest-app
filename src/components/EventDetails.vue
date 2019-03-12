<template>
  <div :class="$style.event">
    <div :class="$style.whiteTitle">
      <h3>Appathon</h3>
    </div>

    <div :class="$style.summary">
      <h4 :class="$style.title">Summary</h4>
      <p :class="$style.text">{{event.summary}}</p>
    </div>

    <div :class="$style.rules">
      <h4 :class="$style.title">Rules</h4>
      <p :class="$style.text">{{event.rules}}</p>
    </div>

    <div :class="$style.ps">
      <h4 :class="$style.title">Problem Statement</h4>
      <p :class="$style.link"><a href="#">{{event.link}}</a></p>
    </div>

    <div :class="$style.contacts">
      <h4 :class="$style.title">Co-ordinators</h4>
      <div :class="$style.container">
        <div :class="$style.stat" v-for="(stat, i) in event.coordinators" :key="i">
          <div :class="$style.name">{{ stat.name }}</div>
          <div :class="$style.email">{{ stat.email }}</div>
        </div>
      </div>
    </div>

    <div :class="$style.faq">
      <h4 :class="$style.title">FAQ</h4>
      <p :class="$style.text">{{event.faq}}</p>
    </div>

  </div>
</template>

<script>
export default {
  data() {
    return {
      event: {
        title: "Appathon",
        summary: "A challenge to blend your creativity and programming skills to develop a robust mobile app.",
        rules: "Coming Soon",
        link: "codefest.tech/appathon",
        coordinators: [
          {
            name: "Mayank Vinod Pathroliya",
            email: "mayank.vpathroliya.cse17@itbhu.ac.in"
          },
          {
            name: "K Gauthamph Motherboard ",
            email: "gauthamph.motherboard.cse17@itbhu.ac.in"
          }
        ],
        faq: "Coming Soon",
      },
    };
  }
};
</script>

<style lang="stylus" module>
@import '../styles/theme.styl';
@import '../styles/anims.styl';
@import '../styles/colors.styl';


.event {

  .whiteTitle {
    color: $white;
    font-family: 'Aldo the Apache';
    margin-top: 30px;
    font-size: 40px;
    text-align: center;
  }
  
  .summary {
    .title {
      font-family: 'Aldo the Apache';
      font-size: 30px;
      margin-top: 20px;
    }
    .text {
      font-size: 20px;
      margin-top: 10px;
      margin-bottom: 10px;
    }
  }

  .rules {
    .title {
      font-family: 'Aldo the Apache';
      font-size: 30px;
      margin-top: 20px;
    }
    .text {
      font-size: 20px;
      margin-top: 10px;
      margin-bottom: 10px;
    }
  }

  .ps {
    .title {
      font-family: 'Aldo the Apache';
      font-size: 30px;
      margin-top: 20px;
    }
    .link {
      text-align: center;
      a {
        color: $chartreuse;
      }    
      font-size: 20px;
      margin-top: 10px;
      margin-bottom: 10px;
    }
  }

  .contacts {
    .title {
      font-family: 'Aldo the Apache';
      font-size: 30px;
      margin-top: 20px;
    }
    .container {
      display: grid;
      grid-template-columns: 50% 50%;
      grid-template-rows: 100px;
      grid-column-gap: 30px;
      grid-row-gap: 50px;
      justify-content: space-evenly;
    }
    .stat{
      .name,.email{
        font-family: 'ubuntu';
        font-weight: bold;
        margin-top: 20px;
        margin-left: auto;
        margin-right: auto;
        text-align: center;
        font-size: 20px;
      }
    }
  }  

  .faq {
    .title {
      font-family: 'Aldo the Apache';
      font-size: 30px;
      margin-top: 20px;
    }
    .text {
      font-size: 20px;
      margin-top: 10px;
      margin-bottom: 10px;
    }
  }
}
</style>
