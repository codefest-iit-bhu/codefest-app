<template>
    <div :class="[$style.card, $style[$mq]]">
      <div :class="$style.cardContainer">
        <div
          :class="$style.cardItem"
          v-for="(item, index) in items"
          :key="index"
          :slot="`item${index}`"
        >
          <div :class="$style.cardBody">
            <div :class="$style.imgContainer">
                <img :src="item.photoUrl" alt="User Photo" :class="$style.cardImg" />
            </div>

            <div :class="$style.cardInfo">
                <div :class="$style.title">
                    <h2>{{ item.name }}</h2>
                    <div :class="$style.icon">
                        <a :href="item.linkedin" target="_blank" rel="noopener noreferrer"><i class="fab fa-linkedin"></i></a>
                    </div>
                </div>
                <p>Portfolio: {{ item.portfolio }}</p>
                    
                <p>Graduation Year: {{ item.graduationYear }}</p>
            </div>
          </div>
        </div>
    </div>
    </div>
  </template>
  
  <script>
  
  export default {
    props: {
      items: {
        type: Array,
        required: true,
      },
    },
  };
  </script>

  
<style module lang="stylus">

  .card {
    .cardContainer {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 70px;
    }
    .cardItem {
      width: 270px;
      height: 400px;

      .cardBody {
        border: 1px;
        border-radius: 25px;
        box-shadow: 0 0px 15px var(--appbar-shadow-color);
        overflow: hidden;
        padding: 20px;
        display: flex; 
        justify-content: center; 
        align-items: center; 
        flex-direction: column;
        height: 100%;

        .imgContainer {       
            width: 240px;
            height: 230px;
            overflow: hidden; 
            display: flex; 
            justify-content: center; 
            align-items: center;
            
            .cardImg {
                width: 100%;
                height: 100%;
                object-fit: cover; 
                border-radius: 25px;
            }
        }
    
        .cardInfo {
            margin-top: 5px;
            width: 240px;
            text-align: left;
            h2 {
                margin-top: 5px;
                font-size: 18px;
                color: var(--text-color);
            }

            .title{
                display: flex;
            }           
        
            p {
                margin: 5px 0;
                font-size: 14px;
                color: var(--text-color);
            }

            a {
                text-decoration: none;
                color: var(--text-color);
                margin-left: 25%;
            }

            .icon {
                text-align: right;
                margin-top: 5px;
            }
        }
    }
    }
  }
</style>
  