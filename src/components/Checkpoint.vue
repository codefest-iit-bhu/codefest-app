<template>
    <div :class="[$style.eventContainer, isDone?$style.done:'', checkpointData.major?$style.major:'']">
        <div :class="$style.dateTime">
            <span v-if="checkpointData.major">
                <i class="fa fa-calendar-alt" aria-hidden="true"></i>
                {{computedDate}}
            </span>
            <span v-else>
                <i class="fa fa-clock" aria-hidden="true"></i>
                {{computedTime}}
            </span>
        </div>
        <div :class="$style.event">
            <!-- <span>
            <img :src="event.image">
            </span> -->
            <span>
            <h4>{{checkpointData.title}}</h4>
            </span>
        </div>
    </div>
</template>

<script>
export default {
props: {
    checkpointData: {
        required: true,
        type: Object
    },
},
computed: {
    isDone() {
        var today = new Date();
        if (this.checkpointData.end) return this.checkpointData.end <= today;
        else return this.checkpointData.start <= today;
    },
    computedDate(){
        var monthNames = [
            "January", "February", "March",
            "April", "May", "June", "July",
            "August", "September", "October",
            "November", "December"
        ];
        var date = this.checkpointData.start;
        var day = date.getDate();
        var monthIndex = date.getMonth();
        var year = date.getFullYear();

        return day + ' ' + monthNames[monthIndex];
    },
    computedTime(){
        var start = this.checkpointData.start;
        var end = this.checkpointData.end;

        if(end){
            return this.formatDate(start)+" - "+this.formatDate(end)
        }
        else return this.formatDate(start)
    }
},
methods: {
    formatDate(date){
        var hours = date.getHours();
        var minutes = date.getMinutes();
        var ampm = hours >= 12 ? 'PM' : 'AM';
        hours = hours % 12;
        hours = hours ? hours : 12;
        minutes = minutes < 10 ? '0'+minutes : minutes;
        var strTime = hours + ':' + minutes + ' ' + ampm;
        return strTime;
    }
}
}
</script>

<style module lang="stylus">

@require '~@styles/theme';
@require '~@styles/anims';

.eventContainer {
    margin: 0 auto;
    padding: 0;
    position: relative;
    height: 100px;

    &:first-child{
        &:before{
            top:0;
        }
    }

    &:last-child{
        &:before {
            top: 0;
        }
        &:after{
            display:none;
        }
    }


    &:before {
        content: '';
        position: absolute;
        width: 15px;
        height: 15px;
        left: -5px
        top: 5px;
        background-color: white;
        border: 1px solid $chartreuse;
        border-radius: 50%;
        z-index: 1;
    }

    &:after {
        content: '';
        position: absolute;
        margin: auto;
        z-index: -2;
        border-right: 5px solid white;
        top: 0;
        bottom: 0;
        left: 0
    }

    &.done {
        &:after {
        border-color: $chartreuse;
        }

        &:before {
        background: $chartreuse;
        }
    }

    &.major{
        &:before{
            
            left: -8px;
            width: 20px;
            height: 20px;
            animation: neon-box 1.5s ease-in-out infinite alternate;
        }
        .dateTime{
            animation: neon-box 1.5s ease-in-out infinite alternate;
            width: 150px;
        }
        
    }
    .dateTime, .event {
        position: relative;
        background: transparent;
        margin: 0;
        color: white;
        border-radius: 4px;
    }

    .dateTime{
        top: 0;
        left: 25px
        width: 200px;
        height: 30px;
        line-height 20px;
        padding: 0 5px;
        margin-bottom: 2px;
        font-size: 14px;
        line-height: 30px;
        text-align: center;
        border: 1px solid $chartreuse;
    }

    .event {
        border-radius: 5px;
        top: 0;
        left: 25px
        padding: 5px;
        height: 60px;
        width: 300px;

        min-width: 100px;

        img {
        width: 30px;
        height: 30px;
        float: left;
        }

        .summary {
        font-size: 12px;
        margin: auto 5px;
        }

        span {
        h4 {
            margin: 0;
            font: 16px Ubuntu;
        }
        }

    }

}
</style>
