<template>
<div class = "register">
<a href = "login">
<i class="fas fa-user-plus" style = "color:black;"><span style = "font-family: 'Aldo the Apache';font-size:18px;" > Register</span></i>
</a>
</div>
</template>

<script>
export default {
   
};
</script>

<style module lang = "stylus" scoped>
@require '~@styles/theme';
div
    a
        position fixed
        width 150px 
        height 60px;
        bottom 40px
        right 40px
        background-color $chartreuse
        color #FFF
        border-radius 50px
        text-align center
        z-index 999
    i
        margin-top 22px
</style>