<template>
    <div :class="$style.container">
        <div :class="$style.brdr">
        <div :class="$style.bck"></div>
            <button :class="$style.btn">
              {{ text }}
            </button>
        </div>
    </div>
    
    
</template>

<script>
// var canvas=document.querySelector('canvas');
// var c=canvas.getContext('2d');
// c.beginPath();
// c.moveTo(150, 25);
// c.lineTo(250, 25);
// c.strokeStyle='rgb(7,249,254)';
// c.stroke();
export default {
    
    name: 'Cards',
    props: {
        text: String,

    },
    
}
</script>

<style module lang="stylus" scoped>
$btn-width=800px;
$btn-height=100px;
$margin=1.5px;
    .container{
        display: flex;
        align-items: center;
        justify-content: center;
        height: $btn-height;

        .brdr{

            position: absolute;
            clip-path: polygon(5% 0,100% 0,100% 70%,95% 100%,0 100%,0 30% );
            margin: -2px auto;
            width: $btn-width;
            height: $btn-height;
            z-index: 11;
            background: rgb(7,249,254);

            .btn{

                border-width: 0px;
                color: rgb(7,249,254);
                position: absolute;
                bottom: 1px;
                left: 2px;
                padding: 0;
                clip-path: polygon(5% 0,100% 0,100% 70%,95% 100%,0 100%,0 30% );
                background: radial-gradient(circle, rgba(7, 249, 254, 0.1), rgba(7, 249, 254, 0.2));
                height: 100%;
                width: $btn-width - 2 * @left;
            }
            .bck{
                background: rgba(0,0,0,1);
                height: 100-((($margin*2)/$btn-height)*100)%;
                width: 100-((($margin*2)/$btn-width)*100)%;
                margin: 1.5px;
                clip-path: polygon(5% 0,100% 0,100% 70%,95% 100%,0 100%,0 30% );
            }
        }
    }
</style>