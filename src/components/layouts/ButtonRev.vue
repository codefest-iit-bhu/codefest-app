<template>
    <div :class="$style.container">
        <div class="svg" style="position: absolute; ">
            <svg height="110" width="350">
                <line x1="60" y1="10" x2="125" y2="10" style="stroke:rgb(7,249,254);stroke-width:1" />
                <circle cx="55" cy="10" r="5" stroke="rgb(7,249,254)" stroke-width="1"  />

                <line x1="110" y1="105" x2="200" y2="105" style="stroke:rgb(7,249,254);stroke-width:1" />
                <line x1="70" y1="80" x2="110" y2="105" style="stroke:rgb(7,249,254);stroke-width:1" />
                <line x1="30" y1="80" x2="70" y2="80" style="stroke:rgb(7,249,254);stroke-width:1" />
                <circle cx="25" cy="80" r="5" stroke="rgb(7,249,254)" stroke-width="1"  />
            </svg>
        </div>
        <div :class="$style.brdr">
        <div :class="$style.bck"></div>
            <button :class="$style.btn">
                {{ text }}
            </button>
        </div>
    </div>
    
    
</template>

<script>
export default {
    name: 'ButtonRev',
    props: {
        text: String,
    }
}
</script>

<style module lang="stylus" scoped>
$btn-width=200px;
$btn-height=80px;
$margin=1.5px;
    .container{
        display: flex;
        align-items: center;
        justify-content: center;
        height: $btn-height;
        .brdr{

            position: absolute;
            clip-path: polygon(0 0,80% 0,100% 30%,100% 100%,20% 100%,0 70% );
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
                clip-path: polygon(0 0,80% 0,100% 30%,100% 100%,20% 100%,0 70% );
                background: radial-gradient(circle, rgba(7, 249, 254, 0.1), rgba(7, 249, 254, 0.2));
                height: 100%;
                width: $btn-width - 2 * @left;
            }
            .bck{
                background: rgba(0,0,0,1);
                height: 100-((($margin*2)/$btn-height)*100)%;
                width: 100-((($margin*2)/$btn-width)*100)%;
                margin: 1.5px;
                clip-path: polygon(0 0,80% 0,100% 30%,100% 100%,20% 100%,0 70% );
            }
        }
    }
</style>