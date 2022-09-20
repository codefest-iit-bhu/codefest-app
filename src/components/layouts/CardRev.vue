<template>
    <div :class="$style.container">
        <div :class="$style.brdr">
        <div :class="$style.bck"></div>
            
            <button :class="$style.btn">
                <span :class="$style.ttl"><strong>{{ title }}</strong></span>
                <p :class="$style.cntnt">{{ text }}</p>
            </button>
        </div>
    </div>
    
    
</template>

<script>
export default {
    name: 'CardRev',
    props: {
        text: String,
        title: String,
    }
}
</script>

<style module lang="stylus" scoped>
$btn-width=800px;
$btn-height=100px;
$margin=1.5px;

    .cntnt{
        display: flex;
        justify-content: flex-end;
        margin-right: 50px;
    }

    .ttl{
        font-size:larger;
        justify-content: flex-end;
        display: flex;
        margin-top: 10px;
        margin-bottom: -15px;
        margin-right: 50px;
    }
    .container{
        display: flex;
        align-items: center;
        justify-content: center;
        height: $btn-height;
        .brdr{

            position: absolute;
            clip-path: polygon(0 0,95% 0,100% 30%,100% 100%,5% 100%,0 70% );
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
                clip-path: polygon(0 0,95% 0,100% 30%,100% 100%,5% 100%,0 70% );
                background: radial-gradient(circle, rgba(7, 249, 254, 0.1), rgba(7, 249, 254, 0.2));
                height: 100%;
                width: $btn-width - 2 * @left;
            }
            .bck{
                background: rgba(0,0,0,1);
                height: 100-((($margin*2)/$btn-height)*100)%;
                width: 100-((($margin*2)/$btn-width)*100)%;
                margin: 1.5px;
                clip-path: polygon(0 0,95% 0,100% 30%,100% 100%,5% 100%,0 70% );
            }
        }
    }
</style>