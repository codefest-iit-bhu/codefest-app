<template>
    <div :class="$style.link">
        <router-link to="/login?redirect=/codestart">
        <div :class="$style.loginButton">
          <i class="fas fa-sign-in-alt" :class="$style.loginLogo"></i>
           Register
        </div>
        </router-link>
    </div>
</template>

<script>
export default {
    methods: {
       
    },
    mounted() {
        this.$emit("mounted");
    }
};
</script>

<style module lang="stylus">
$login-color = #1a73e8;

.link {
  margin: auto;
  margin-top: 10px;
  max-width: 312px;
  height: auto;
  padding: 10px;
  
  border-radius: 5px
  text-align: center;
  cursor: pointer;
  background-color: $login-color;
}

.loginButton {
  display: flex;
  justify-content: center;
  color: white;
  
}
a:hover{ 
    text-decoration: none; 
}
.loginLogo {
    font-size: 25px;
    margin-right: 10px;
   
}
</style>

// #1a73e8