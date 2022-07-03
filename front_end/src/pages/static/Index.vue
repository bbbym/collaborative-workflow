<template>
  <q-page class="flex flex-center flex-direction-vertical">
    <div class="text-h4 page-title1">collaborative workflow</div>
    <div class="text-h7 text-weight-medium text-center page-title2">
<!--      呼啦圈工作室研究发现，不同性格特征的人在团队协作的过程中倾向于不同的思考和互动方式，<br />Providing-->
<!--      such spaces will benefit team work, its members and advance what-->
<!--      collaborative workflow can and may be.-->
    </div>
    <div class="row">
      <div
        class="col-lg-5 offset-lg-1 wow bounceInUp"
        data-wow-duration="1.4s"
        style="
          visibility: visible;
          animation-duration: 1.4s;
          animation-name: bounceInUp;
        "
      >
        <div class="box">
          <div
            class="text-h6"
            style="font-weight: bolder; position: absolute; z-index: 1"
          >
            Think aloud
          </div>
          <p
            class="description"
            style="
              position: absolute;
              z-index: 1;
              position: relative;
              top: 30px;
              margin-bottom: 30px;
            "
          >
            This type of contemplative activity is critical for fostering
            resilience, as well as cultivating creativity and intellectual
            growth.The trend of team work makes us long for moments in which to
            rebalance and compose our thoughts, bodies and selfness,
            companionably and creatively with others. It is therefore that we
            believe that silence is critical for fostering personal and
            collective resilience, creativity, and intellectual growth.
          </p>
          <div class="icon">
            <img
              src="../../assets/公告.png"
              style="
                height: 280px;
                position: relative;
                top: -100px;
                left: -8px;
                position: absolute;
                z-index: 0;
              "
            />
          </div>
        </div>
      </div>
      <div
        class="col-lg-5 wow bounceInUp"
        data-wow-duration="1.4s"
        style="
          visibility: visible;
          animation-duration: 1.4s;
          animation-name: bounceInUp;
        "
      >
        <div class="box">
          <div
            class="text-h6"
            style="font-weight: bolder; position: absolute; z-index: 1"
          >
            Think silent
          </div>
          <p
            class="description"
            style="
              position: absolute;
              z-index: 1;
              position: relative;
              top: 30px;
              margin-bottom: 30px;
            "
          >
            This type of contemplative activity is critical for fostering
            resilience, as well as cultivating creativity and intellectual
            growth.The trend of team work makes us long for moments in which to
            rebalance and compose our thoughts, bodies and selfness,
            companionably and creatively with others. It is therefore that we
            believe that silence is critical for fostering personal and
            collective resilience, creativity, and intellectual growth.
          </p>
          <div class="icon">
            <img
              src="../../assets/静音.png"
              style="
                height: 280px;
                position: relative;
                top: -100px;
                left: -0px;
                position: absolute;
                z-index: 0;
              "
            />
          </div>
        </div>
      </div>
    </div>
    <div class="flex flex-direction-horizontal" margin-top="0px">
      <q-btn
        unelevated
        rounded
        label="Start Working"
        @click="this.$router.push('/usage')"
        class="button-begin"
      />
      <q-btn
        unelevated
        rounded
        label="Personality Test"
        @click="toSwitch"
        href="http://www.apesk.com/bigfive/"
        class="bttn-unite"
      />
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "PageIndex",
  methods: {
    toSwitch() {
      document.getElementById("mac").scrollIntoView({
        behavior: "smooth",
      });
    },
  },
});
</script>
<style lang="scss" scoped>
.page-title1 {
  color: #202d3f;
  margin-top: 40px;
  font-weight: 600;
}

.page-title2 {
  line-height: 1.5;
  color: #202d3f;
  margin-top: 27px;
  font-weight: 400;
}

.page-title3 {
  display: flex;
  align-items: center;
  color: #fbfbfb;
  margin-top: 13px;
}

.page-title3:before {
  border-bottom: 2px solid #fbfbfb;
  content: "";
  width: 32px;
  display: block;
  margin: 0.5em 1rem;
  height: 1px;
}

.page-title3:after {
  border-bottom: 2px solid #fbfbfb;
  content: "";
  width: 32px;
  display: block;
  margin: 0.5em 1rem;
  height: 1px;
}

.button-begin {
  margin-top: 58px;
  color: white;
  background-color: #0d61fe;
  margin-left: 60px;
  cursor: pointer;
  position: relative;
  font-size: 20px;
  font-family: inherit;
  padding: 5px 20px;
  overflow: hidden;
  border-radius: 100px;
  color: #ffffff;
  -webkit-transition: color 0.3s cubic-bezier(0.02, 0.01, 0.47, 1),
    border-color 0.3s cubic-bezier(0.02, 0.01, 0.47, 1);
  transition: color 0.3s cubic-bezier(0.02, 0.01, 0.47, 1),
    border-color 0.3s cubic-bezier(0.02, 0.01, 0.47, 1);
}

.button-learn {
  margin-left: 60px;
  margin-top: 58px;
  padding: 16px 32px 16px 32px;
  color: #0d61fe;
  border-color: #0d61fe;
  background-color: #abafc7;
}

.content-mac-container {
  background: transparent;
  margin-top: 63px;
}

.content-mac-container-question-answer-container {
  background: transparent;
}

.content-mac-container-question-container {
  width: 661px;
  height: 133px;
  margin-left: 23px;
  margin-top: 64px;
  background: #fafafa;
  border-radius: 20px;
}

.text-color-black {
  color: #000000;
}

.text-color-pink {
  color: #0d61fe;
}

.content-mac-container-explanation {
  line-height: 1.8rem;
  letter-spacing: 0.1rem;
  margin-top: 24px;
  margin-left: 172px;
  width: 600px;
  color: #e6e6e6;
}

.content-mac-left-container {
  padding-left: 172px;
  margin-top: 80px;
}

.content-mac-left-icon {
  width: 37px;
  height: 40px;
}

.content-mac-left-title {
  margin-top: 16px;
}

.content-mac-left-text {
  line-height: 1.5rem;
  margin-top: 16px;
  color: #e6e6e6;
  width: 320px;
}

.content-mac-right-container {
  padding-left: 60px;
  margin-top: 80px;
}

.content-mac-right-icon {
  width: 37px;
  height: 40px;
}

.content-mac-right-title {
  margin-top: 16px;
}

.content-mac-right-text {
  line-height: 1.5rem;
  margin-top: 16px;
  color: #e6e6e6;
  width: 320px;
}

.content-gradient-container {
  margin-top: 32px;
  width: 96%;
  height: 3300px;
  background: linear-gradient(
    180deg,
    rgba(52, 10, 121, 0.01) 0%,
    rgba(96, 1, 211, 0.41) 100%
  );
  box-shadow: -10px 15px 50px rgba(96, 1, 211, 0.302);
  border-radius: 16px;
}

.content-gradient-title {
  background: #ffffff;
  opacity: 0.9;
  color: #0d61fe;
  border: 1px solid #ffffff;
  box-sizing: border-box;
  border-radius: 7px;
  width: 180px;
  height: 40px;
  margin-top: 200px;
}

.content-gradient-title1 {
  color: #fff;
  margin-top: 54px;
}

.content-gradient-title2 {
  letter-spacing: 0.1rem;
  line-height: 2rem;
  margin-top: 34px;
  color: #fbfbfb;
}

.content-gradient-container1 {
  margin-top: 100px;
  height: 600px;
  background-size: 60% !important;
  background: url("../../assets/img1.png") no-repeat right 68px center;
  width: 100%;
}

.content-gradient-container1-content {
  margin-top: 150px;
  margin-left: 108px;
  background: transparent;
  color: white;
}

.content-gradient-container1-content-text {
  letter-spacing: 0.1rem;
  margin-top: 48px;
  line-height: 2rem;
}

.content-gradient-container2 {
  justify-content: flex-end;
  margin-top: 100px;
  height: 600px;
  background-size: 60% !important;
  background: url("../../assets/img2.png") no-repeat left 68px center;
  width: 100%;
}

.content-gradient-container2-content {
  margin-right: 108px;
  margin-top: 150px;
  background: transparent;
  color: white;
}

.content-gradient-container2-content-text {
  letter-spacing: 0.1rem;
  margin-top: 48px;
  line-height: 2rem;
}

.content-gradient-container3 {
  margin-top: 100px;
  height: 600px;
  background-size: 60% !important;
  background: url("../../assets/img3.png") no-repeat right 68px center;
  width: 100%;
}

.content-gradient-container3-content {
  margin-top: 320px;
  margin-left: 108px;
  background: transparent;
  color: white;
}

.content-gradient-container3-content-text {
  letter-spacing: 0.1rem;
  margin-top: 48px;
  line-height: 2rem;
}

.content-gradient-container4 {
  justify-content: flex-end;
  margin-top: 100px;
  height: 600px;
  background-size: 60% !important;
  background: url("../../assets/img4.png") no-repeat left 68px center;
  width: 100%;
}

.content-gradient-container4-content {
  margin-right: 108px;
  background: transparent;
  color: white;
}

.content-gradient-container4-content-text {
  letter-spacing: 0.1rem;
  margin-top: 48px;
  line-height: 2rem;
}

.content-gradient-content1 {
  margin-top: 32px;
}

.content-gradient-content1-title {
  margin-left: 16px;
}

.content-gradient-container1-right {
  margin-left: 108px;
}

.animated {
  animation-duration: 1s;
  animation-fill-mode: both;
}
.animated.infinite {
  animation-iteration-count: infinite;
}
.animated.hinge {
  animation-duration: 2s;
}
.animated.bounceIn,
.animated.bounceOut,
.animated.flipOutX,
.animated.flipOutY {
  animation-duration: 0.75s;
}
@keyframes bounce {
  0%,
  20%,
  53%,
  80%,
  to {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
    transform: translateZ(0);
  }
  40%,
  43% {
    animation-timing-function: cubic-bezier(0.755, 0.05, 0.855, 0.06);
    transform: translate3d(0, -30px, 0);
  }
  70% {
    animation-timing-function: cubic-bezier(0.755, 0.05, 0.855, 0.06);
    transform: translate3d(0, -15px, 0);
  }
  90% {
    transform: translate3d(0, -4px, 0);
  }
}
.bounce {
  animation-name: bounce;
  transform-origin: center bottom;
}
@keyframes flash {
  0%,
  50%,
  to {
    opacity: 1;
  }
  25%,
  75% {
    opacity: 0;
  }
}
.flash {
  animation-name: flash;
}
@keyframes pulse {
  0% {
    transform: scaleX(1);
  }
  50% {
    transform: scale3d(1.05, 1.05, 1.05);
  }
  to {
    transform: scaleX(1);
  }
}
.pulse {
  animation-name: pulse;
}
@keyframes rubberBand {
  0% {
    transform: scaleX(1);
  }
  30% {
    transform: scale3d(1.25, 0.75, 1);
  }
  40% {
    transform: scale3d(0.75, 1.25, 1);
  }
  50% {
    transform: scale3d(1.15, 0.85, 1);
  }
  65% {
    transform: scale3d(0.95, 1.05, 1);
  }
  75% {
    transform: scale3d(1.05, 0.95, 1);
  }
  to {
    transform: scaleX(1);
  }
}
.rubberBand {
  animation-name: rubberBand;
}
@keyframes shake {
  0%,
  to {
    transform: translateZ(0);
  }
  10%,
  30%,
  50%,
  70%,
  90% {
    transform: translate3d(-10px, 0, 0);
  }
  20%,
  40%,
  60%,
  80% {
    transform: translate3d(10px, 0, 0);
  }
}
.shake {
  animation-name: shake;
}
@keyframes headShake {
  0% {
    transform: translateX(0);
  }
  6.5% {
    transform: translateX(-6px) rotateY(-9deg);
  }
  18.5% {
    transform: translateX(5px) rotateY(7deg);
  }
  31.5% {
    transform: translateX(-3px) rotateY(-5deg);
  }
  43.5% {
    transform: translateX(2px) rotateY(3deg);
  }
  50% {
    transform: translateX(0);
  }
}
.headShake {
  animation-timing-function: ease-in-out;
  animation-name: headShake;
}
@keyframes swing {
  20% {
    transform: rotate(15deg);
  }
  40% {
    transform: rotate(-10deg);
  }
  60% {
    transform: rotate(5deg);
  }
  80% {
    transform: rotate(-5deg);
  }
  to {
    transform: rotate(0deg);
  }
}
.swing {
  transform-origin: top center;
  animation-name: swing;
}
@keyframes tada {
  0% {
    transform: scaleX(1);
  }
  10%,
  20% {
    transform: scale3d(0.9, 0.9, 0.9) rotate(-3deg);
  }
  30%,
  50%,
  70%,
  90% {
    transform: scale3d(1.1, 1.1, 1.1) rotate(3deg);
  }
  40%,
  60%,
  80% {
    transform: scale3d(1.1, 1.1, 1.1) rotate(-3deg);
  }
  to {
    transform: scaleX(1);
  }
}
.tada {
  animation-name: tada;
}
@keyframes wobble {
  0% {
    transform: none;
  }
  15% {
    transform: translate3d(-25%, 0, 0) rotate(-5deg);
  }
  30% {
    transform: translate3d(20%, 0, 0) rotate(3deg);
  }
  45% {
    transform: translate3d(-15%, 0, 0) rotate(-3deg);
  }
  60% {
    transform: translate3d(10%, 0, 0) rotate(2deg);
  }
  75% {
    transform: translate3d(-5%, 0, 0) rotate(-1deg);
  }
  to {
    transform: none;
  }
}
.wobble {
  animation-name: wobble;
}
@keyframes jello {
  0%,
  11.1%,
  to {
    transform: none;
  }
  22.2% {
    transform: skewX(-12.5deg) skewY(-12.5deg);
  }
  33.3% {
    transform: skewX(6.25deg) skewY(6.25deg);
  }
  44.4% {
    transform: skewX(-3.125deg) skewY(-3.125deg);
  }
  55.5% {
    transform: skewX(1.5625deg) skewY(1.5625deg);
  }
  66.6% {
    transform: skewX(-0.78125deg) skewY(-0.78125deg);
  }
  77.7% {
    transform: skewX(0.390625deg) skewY(0.390625deg);
  }
  88.8% {
    transform: skewX(-0.1953125deg) skewY(-0.1953125deg);
  }
}
.jello {
  animation-name: jello;
  transform-origin: center;
}
@keyframes bounceIn {
  0%,
  20%,
  40%,
  60%,
  80%,
  to {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  0% {
    opacity: 0;
    transform: scale3d(0.3, 0.3, 0.3);
  }
  20% {
    transform: scale3d(1.1, 1.1, 1.1);
  }
  40% {
    transform: scale3d(0.9, 0.9, 0.9);
  }
  60% {
    opacity: 1;
    transform: scale3d(1.03, 1.03, 1.03);
  }
  80% {
    transform: scale3d(0.97, 0.97, 0.97);
  }
  to {
    opacity: 1;
    transform: scaleX(1);
  }
}
.bounceIn {
  animation-name: bounceIn;
}
@keyframes bounceInDown {
  0%,
  60%,
  75%,
  90%,
  to {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  0% {
    opacity: 0;
    transform: translate3d(0, -3000px, 0);
  }
  60% {
    opacity: 1;
    transform: translate3d(0, 25px, 0);
  }
  75% {
    transform: translate3d(0, -10px, 0);
  }
  90% {
    transform: translate3d(0, 5px, 0);
  }
  to {
    transform: none;
  }
}
.bounceInDown {
  animation-name: bounceInDown;
}
@keyframes bounceInLeft {
  0%,
  60%,
  75%,
  90%,
  to {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  0% {
    opacity: 0;
    transform: translate3d(-3000px, 0, 0);
  }
  60% {
    opacity: 1;
    transform: translate3d(25px, 0, 0);
  }
  75% {
    transform: translate3d(-10px, 0, 0);
  }
  90% {
    transform: translate3d(5px, 0, 0);
  }
  to {
    transform: none;
  }
}
.bounceInLeft {
  animation-name: bounceInLeft;
}
@keyframes bounceInRight {
  0%,
  60%,
  75%,
  90%,
  to {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  0% {
    opacity: 0;
    transform: translate3d(3000px, 0, 0);
  }
  60% {
    opacity: 1;
    transform: translate3d(-25px, 0, 0);
  }
  75% {
    transform: translate3d(10px, 0, 0);
  }
  90% {
    transform: translate3d(-5px, 0, 0);
  }
  to {
    transform: none;
  }
}
.bounceInRight {
  animation-name: bounceInRight;
}
@keyframes bounceInUp {
  0%,
  60%,
  75%,
  90%,
  to {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }
  0% {
    opacity: 0;
    transform: translate3d(0, 3000px, 0);
  }
  60% {
    opacity: 1;
    transform: translate3d(0, -20px, 0);
  }
  75% {
    transform: translate3d(0, 10px, 0);
  }
  90% {
    transform: translate3d(0, -5px, 0);
  }
  to {
    transform: translateZ(0);
  }
}
.bounceInUp {
  animation-name: bounceInUp;
}
@keyframes bounceOut {
  20% {
    transform: scale3d(0.9, 0.9, 0.9);
  }
  50%,
  55% {
    opacity: 1;
    transform: scale3d(1.1, 1.1, 1.1);
  }
  to {
    opacity: 0;
    transform: scale3d(0.3, 0.3, 0.3);
  }
}
.bounceOut {
  animation-name: bounceOut;
}
@keyframes bounceOutDown {
  20% {
    transform: translate3d(0, 10px, 0);
  }
  40%,
  45% {
    opacity: 1;
    transform: translate3d(0, -20px, 0);
  }
  to {
    opacity: 0;
    transform: translate3d(0, 2000px, 0);
  }
}
.bounceOutDown {
  animation-name: bounceOutDown;
}
@keyframes bounceOutLeft {
  20% {
    opacity: 1;
    transform: translate3d(20px, 0, 0);
  }
  to {
    opacity: 0;
    transform: translate3d(-2000px, 0, 0);
  }
}
.bounceOutLeft {
  animation-name: bounceOutLeft;
}
@keyframes bounceOutRight {
  20% {
    opacity: 1;
    transform: translate3d(-20px, 0, 0);
  }
  to {
    opacity: 0;
    transform: translate3d(2000px, 0, 0);
  }
}
.bounceOutRight {
  animation-name: bounceOutRight;
}
@keyframes bounceOutUp {
  20% {
    transform: translate3d(0, -10px, 0);
  }
  40%,
  45% {
    opacity: 1;
    transform: translate3d(0, 20px, 0);
  }
  to {
    opacity: 0;
    transform: translate3d(0, -2000px, 0);
  }
}
.bounceOutUp {
  animation-name: bounceOutUp;
}
@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
.fadeIn {
  animation-name: fadeIn;
}
@keyframes fadeInDown {
  0% {
    opacity: 0;
    transform: translate3d(0, -100%, 0);
  }
  to {
    opacity: 1;
    transform: none;
  }
}
.fadeInDown {
  animation-name: fadeInDown;
}
@keyframes fadeInDownBig {
  0% {
    opacity: 0;
    transform: translate3d(0, -2000px, 0);
  }
  to {
    opacity: 1;
    transform: none;
  }
}
.fadeInDownBig {
  animation-name: fadeInDownBig;
}
@keyframes fadeInLeft {
  0% {
    opacity: 0;
    transform: translate3d(-100%, 0, 0);
  }
  to {
    opacity: 1;
    transform: none;
  }
}
.fadeInLeft {
  animation-name: fadeInLeft;
}
@keyframes fadeInLeftBig {
  0% {
    opacity: 0;
    transform: translate3d(-2000px, 0, 0);
  }
  to {
    opacity: 1;
    transform: none;
  }
}
.fadeInLeftBig {
  animation-name: fadeInLeftBig;
}
@keyframes fadeInRight {
  0% {
    opacity: 0;
    transform: translate3d(100%, 0, 0);
  }
  to {
    opacity: 1;
    transform: none;
  }
}
.fadeInRight {
  animation-name: fadeInRight;
}
@keyframes fadeInRightBig {
  0% {
    opacity: 0;
    transform: translate3d(2000px, 0, 0);
  }
  to {
    opacity: 1;
    transform: none;
  }
}
.fadeInRightBig {
  animation-name: fadeInRightBig;
}
@keyframes fadeInUp {
  0% {
    opacity: 0;
    transform: translate3d(0, 100%, 0);
  }
  to {
    opacity: 1;
    transform: none;
  }
}
.fadeInUp {
  animation-name: fadeInUp;
}
@keyframes fadeInUpBig {
  0% {
    opacity: 0;
    transform: translate3d(0, 2000px, 0);
  }
  to {
    opacity: 1;
    transform: none;
  }
}
.fadeInUpBig {
  animation-name: fadeInUpBig;
}
@keyframes fadeOut {
  0% {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
.fadeOut {
  animation-name: fadeOut;
}
@keyframes fadeOutDown {
  0% {
    opacity: 1;
  }
  to {
    opacity: 0;
    transform: translate3d(0, 100%, 0);
  }
}
.fadeOutDown {
  animation-name: fadeOutDown;
}
@keyframes fadeOutDownBig {
  0% {
    opacity: 1;
  }
  to {
    opacity: 0;
    transform: translate3d(0, 2000px, 0);
  }
}
.fadeOutDownBig {
  animation-name: fadeOutDownBig;
}
@keyframes fadeOutLeft {
  0% {
    opacity: 1;
  }
  to {
    opacity: 0;
    transform: translate3d(-100%, 0, 0);
  }
}
.fadeOutLeft {
  animation-name: fadeOutLeft;
}
@keyframes fadeOutLeftBig {
  0% {
    opacity: 1;
  }
  to {
    opacity: 0;
    transform: translate3d(-2000px, 0, 0);
  }
}
.fadeOutLeftBig {
  animation-name: fadeOutLeftBig;
}
@keyframes fadeOutRight {
  0% {
    opacity: 1;
  }
  to {
    opacity: 0;
    transform: translate3d(100%, 0, 0);
  }
}
.fadeOutRight {
  animation-name: fadeOutRight;
}
@keyframes fadeOutRightBig {
  0% {
    opacity: 1;
  }
  to {
    opacity: 0;
    transform: translate3d(2000px, 0, 0);
  }
}
.fadeOutRightBig {
  animation-name: fadeOutRightBig;
}
@keyframes fadeOutUp {
  0% {
    opacity: 1;
  }
  to {
    opacity: 0;
    transform: translate3d(0, -100%, 0);
  }
}
.fadeOutUp {
  animation-name: fadeOutUp;
}
@keyframes fadeOutUpBig {
  0% {
    opacity: 1;
  }
  to {
    opacity: 0;
    transform: translate3d(0, -2000px, 0);
  }
}
.fadeOutUpBig {
  animation-name: fadeOutUpBig;
}
@keyframes flip {
  0% {
    transform: perspective(400px) rotateY(-1turn);
    animation-timing-function: ease-out;
  }
  40% {
    transform: perspective(400px) translateZ(150px) rotateY(-190deg);
    animation-timing-function: ease-out;
  }
  50% {
    transform: perspective(400px) translateZ(150px) rotateY(-170deg);
    animation-timing-function: ease-in;
  }
  80% {
    transform: perspective(400px) scale3d(0.95, 0.95, 0.95);
    animation-timing-function: ease-in;
  }
  to {
    transform: perspective(400px);
    animation-timing-function: ease-in;
  }
}
.animated.flip {
  -webkit-backface-visibility: visible;
  backface-visibility: visible;
  animation-name: flip;
}
@keyframes flipInX {
  0% {
    transform: perspective(400px) rotateX(90deg);
    animation-timing-function: ease-in;
    opacity: 0;
  }
  40% {
    transform: perspective(400px) rotateX(-20deg);
    animation-timing-function: ease-in;
  }
  60% {
    transform: perspective(400px) rotateX(10deg);
    opacity: 1;
  }
  80% {
    transform: perspective(400px) rotateX(-5deg);
  }
  to {
    transform: perspective(400px);
  }
}
.flipInX {
  -webkit-backface-visibility: visible !important;
  backface-visibility: visible !important;
  animation-name: flipInX;
}
@keyframes flipInY {
  0% {
    transform: perspective(400px) rotateY(90deg);
    animation-timing-function: ease-in;
    opacity: 0;
  }
  40% {
    transform: perspective(400px) rotateY(-20deg);
    animation-timing-function: ease-in;
  }
  60% {
    transform: perspective(400px) rotateY(10deg);
    opacity: 1;
  }
  80% {
    transform: perspective(400px) rotateY(-5deg);
  }
  to {
    transform: perspective(400px);
  }
}
.flipInY {
  -webkit-backface-visibility: visible !important;
  backface-visibility: visible !important;
  animation-name: flipInY;
}
@keyframes flipOutX {
  0% {
    transform: perspective(400px);
  }
  30% {
    transform: perspective(400px) rotateX(-20deg);
    opacity: 1;
  }
  to {
    transform: perspective(400px) rotateX(90deg);
    opacity: 0;
  }
}
.flipOutX {
  animation-name: flipOutX;
  -webkit-backface-visibility: visible !important;
  backface-visibility: visible !important;
}
@keyframes flipOutY {
  0% {
    transform: perspective(400px);
  }
  30% {
    transform: perspective(400px) rotateY(-15deg);
    opacity: 1;
  }
  to {
    transform: perspective(400px) rotateY(90deg);
    opacity: 0;
  }
}
.flipOutY {
  -webkit-backface-visibility: visible !important;
  backface-visibility: visible !important;
  animation-name: flipOutY;
}
@keyframes lightSpeedIn {
  0% {
    transform: translate3d(100%, 0, 0) skewX(-30deg);
    opacity: 0;
  }
  60% {
    transform: skewX(20deg);
    opacity: 1;
  }
  80% {
    transform: skewX(-5deg);
    opacity: 1;
  }
  to {
    transform: none;
    opacity: 1;
  }
}
.lightSpeedIn {
  animation-name: lightSpeedIn;
  animation-timing-function: ease-out;
}
@keyframes lightSpeedOut {
  0% {
    opacity: 1;
  }
  to {
    transform: translate3d(100%, 0, 0) skewX(30deg);
    opacity: 0;
  }
}
.lightSpeedOut {
  animation-name: lightSpeedOut;
  animation-timing-function: ease-in;
}
@keyframes rotateIn {
  0% {
    transform-origin: center;
    transform: rotate(-200deg);
    opacity: 0;
  }
  to {
    transform-origin: center;
    transform: none;
    opacity: 1;
  }
}
.rotateIn {
  animation-name: rotateIn;
}
@keyframes rotateInDownLeft {
  0% {
    transform-origin: left bottom;
    transform: rotate(-45deg);
    opacity: 0;
  }
  to {
    transform-origin: left bottom;
    transform: none;
    opacity: 1;
  }
}
.rotateInDownLeft {
  animation-name: rotateInDownLeft;
}
@keyframes rotateInDownRight {
  0% {
    transform-origin: right bottom;
    transform: rotate(45deg);
    opacity: 0;
  }
  to {
    transform-origin: right bottom;
    transform: none;
    opacity: 1;
  }
}
.rotateInDownRight {
  animation-name: rotateInDownRight;
}
@keyframes rotateInUpLeft {
  0% {
    transform-origin: left bottom;
    transform: rotate(45deg);
    opacity: 0;
  }
  to {
    transform-origin: left bottom;
    transform: none;
    opacity: 1;
  }
}
.rotateInUpLeft {
  animation-name: rotateInUpLeft;
}
@keyframes rotateInUpRight {
  0% {
    transform-origin: right bottom;
    transform: rotate(-90deg);
    opacity: 0;
  }
  to {
    transform-origin: right bottom;
    transform: none;
    opacity: 1;
  }
}
.rotateInUpRight {
  animation-name: rotateInUpRight;
}
@keyframes rotateOut {
  0% {
    transform-origin: center;
    opacity: 1;
  }
  to {
    transform-origin: center;
    transform: rotate(200deg);
    opacity: 0;
  }
}
.rotateOut {
  animation-name: rotateOut;
}
@keyframes rotateOutDownLeft {
  0% {
    transform-origin: left bottom;
    opacity: 1;
  }
  to {
    transform-origin: left bottom;
    transform: rotate(45deg);
    opacity: 0;
  }
}
.rotateOutDownLeft {
  animation-name: rotateOutDownLeft;
}
@keyframes rotateOutDownRight {
  0% {
    transform-origin: right bottom;
    opacity: 1;
  }
  to {
    transform-origin: right bottom;
    transform: rotate(-45deg);
    opacity: 0;
  }
}
.rotateOutDownRight {
  animation-name: rotateOutDownRight;
}
@keyframes rotateOutUpLeft {
  0% {
    transform-origin: left bottom;
    opacity: 1;
  }
  to {
    transform-origin: left bottom;
    transform: rotate(-45deg);
    opacity: 0;
  }
}
.rotateOutUpLeft {
  animation-name: rotateOutUpLeft;
}
@keyframes rotateOutUpRight {
  0% {
    transform-origin: right bottom;
    opacity: 1;
  }
  to {
    transform-origin: right bottom;
    transform: rotate(90deg);
    opacity: 0;
  }
}
.rotateOutUpRight {
  animation-name: rotateOutUpRight;
}
@keyframes hinge {
  0% {
    transform-origin: top left;
    animation-timing-function: ease-in-out;
  }
  20%,
  60% {
    transform: rotate(80deg);
    transform-origin: top left;
    animation-timing-function: ease-in-out;
  }
  40%,
  80% {
    transform: rotate(60deg);
    transform-origin: top left;
    animation-timing-function: ease-in-out;
    opacity: 1;
  }
  to {
    transform: translate3d(0, 700px, 0);
    opacity: 0;
  }
}
.hinge {
  animation-name: hinge;
}
@keyframes jackInTheBox {
  0% {
    opacity: 0;
    transform: scale(0.1) rotate(30deg);
    transform-origin: center bottom;
  }
  50% {
    transform: rotate(-10deg);
  }
  70% {
    transform: rotate(3deg);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}
.jackInTheBox {
  animation-name: jackInTheBox;
}
@keyframes rollIn {
  0% {
    opacity: 0;
    transform: translate3d(-100%, 0, 0) rotate(-120deg);
  }
  to {
    opacity: 1;
    transform: none;
  }
}
.rollIn {
  animation-name: rollIn;
}
@keyframes rollOut {
  0% {
    opacity: 1;
  }
  to {
    opacity: 0;
    transform: translate3d(100%, 0, 0) rotate(120deg);
  }
}
.rollOut {
  animation-name: rollOut;
}
@keyframes zoomIn {
  0% {
    opacity: 0;
    transform: scale3d(0.3, 0.3, 0.3);
  }
  50% {
    opacity: 1;
  }
}
.zoomIn {
  animation-name: zoomIn;
}
@keyframes zoomInDown {
  0% {
    opacity: 0;
    transform: scale3d(0.1, 0.1, 0.1) translate3d(0, -1000px, 0);
    animation-timing-function: cubic-bezier(0.55, 0.055, 0.675, 0.19);
  }
  60% {
    opacity: 1;
    transform: scale3d(0.475, 0.475, 0.475) translate3d(0, 60px, 0);
    animation-timing-function: cubic-bezier(0.175, 0.885, 0.32, 1);
  }
}
.zoomInDown {
  animation-name: zoomInDown;
}
@keyframes zoomInLeft {
  0% {
    opacity: 0;
    transform: scale3d(0.1, 0.1, 0.1) translate3d(-1000px, 0, 0);
    animation-timing-function: cubic-bezier(0.55, 0.055, 0.675, 0.19);
  }
  60% {
    opacity: 1;
    transform: scale3d(0.475, 0.475, 0.475) translate3d(10px, 0, 0);
    animation-timing-function: cubic-bezier(0.175, 0.885, 0.32, 1);
  }
}
.zoomInLeft {
  animation-name: zoomInLeft;
}
@keyframes zoomInRight {
  0% {
    opacity: 0;
    transform: scale3d(0.1, 0.1, 0.1) translate3d(1000px, 0, 0);
    animation-timing-function: cubic-bezier(0.55, 0.055, 0.675, 0.19);
  }
  60% {
    opacity: 1;
    transform: scale3d(0.475, 0.475, 0.475) translate3d(-10px, 0, 0);
    animation-timing-function: cubic-bezier(0.175, 0.885, 0.32, 1);
  }
}
.zoomInRight {
  animation-name: zoomInRight;
}
@keyframes zoomInUp {
  0% {
    opacity: 0;
    transform: scale3d(0.1, 0.1, 0.1) translate3d(0, 1000px, 0);
    animation-timing-function: cubic-bezier(0.55, 0.055, 0.675, 0.19);
  }
  60% {
    opacity: 1;
    transform: scale3d(0.475, 0.475, 0.475) translate3d(0, -60px, 0);
    animation-timing-function: cubic-bezier(0.175, 0.885, 0.32, 1);
  }
}
.zoomInUp {
  animation-name: zoomInUp;
}
@keyframes zoomOut {
  0% {
    opacity: 1;
  }
  50% {
    opacity: 0;
    transform: scale3d(0.3, 0.3, 0.3);
  }
  to {
    opacity: 0;
  }
}
.zoomOut {
  animation-name: zoomOut;
}
@keyframes zoomOutDown {
  40% {
    opacity: 1;
    transform: scale3d(0.475, 0.475, 0.475) translate3d(0, -60px, 0);
    animation-timing-function: cubic-bezier(0.55, 0.055, 0.675, 0.19);
  }
  to {
    opacity: 0;
    transform: scale3d(0.1, 0.1, 0.1) translate3d(0, 2000px, 0);
    transform-origin: center bottom;
    animation-timing-function: cubic-bezier(0.175, 0.885, 0.32, 1);
  }
}
.zoomOutDown {
  animation-name: zoomOutDown;
}
@keyframes zoomOutLeft {
  40% {
    opacity: 1;
    transform: scale3d(0.475, 0.475, 0.475) translate3d(42px, 0, 0);
  }
  to {
    opacity: 0;
    transform: scale(0.1) translate3d(-2000px, 0, 0);
    transform-origin: left center;
  }
}
.zoomOutLeft {
  animation-name: zoomOutLeft;
}
@keyframes zoomOutRight {
  40% {
    opacity: 1;
    transform: scale3d(0.475, 0.475, 0.475) translate3d(-42px, 0, 0);
  }
  to {
    opacity: 0;
    transform: scale(0.1) translate3d(2000px, 0, 0);
    transform-origin: right center;
  }
}
.zoomOutRight {
  animation-name: zoomOutRight;
}
@keyframes zoomOutUp {
  40% {
    opacity: 1;
    transform: scale3d(0.475, 0.475, 0.475) translate3d(0, 60px, 0);
    animation-timing-function: cubic-bezier(0.55, 0.055, 0.675, 0.19);
  }
  to {
    opacity: 0;
    transform: scale3d(0.1, 0.1, 0.1) translate3d(0, -2000px, 0);
    transform-origin: center bottom;
    animation-timing-function: cubic-bezier(0.175, 0.885, 0.32, 1);
  }
}
.zoomOutUp {
  animation-name: zoomOutUp;
}
@keyframes slideInDown {
  0% {
    transform: translate3d(0, -100%, 0);
    visibility: visible;
  }
  to {
    transform: translateZ(0);
  }
}
.slideInDown {
  animation-name: slideInDown;
}
@keyframes slideInLeft {
  0% {
    transform: translate3d(-100%, 0, 0);
    visibility: visible;
  }
  to {
    transform: translateZ(0);
  }
}
.slideInLeft {
  animation-name: slideInLeft;
}
@keyframes slideInRight {
  0% {
    transform: translate3d(100%, 0, 0);
    visibility: visible;
  }
  to {
    transform: translateZ(0);
  }
}
.slideInRight {
  animation-name: slideInRight;
}
@keyframes slideInUp {
  0% {
    transform: translate3d(0, 100%, 0);
    visibility: visible;
  }
  to {
    transform: translateZ(0);
  }
}
.slideInUp {
  animation-name: slideInUp;
}
@keyframes slideOutDown {
  0% {
    transform: translateZ(0);
  }
  to {
    visibility: hidden;
    transform: translate3d(0, 100%, 0);
  }
}
.slideOutDown {
  animation-name: slideOutDown;
}
@keyframes slideOutLeft {
  0% {
    transform: translateZ(0);
  }
  to {
    visibility: hidden;
    transform: translate3d(-100%, 0, 0);
  }
}
.slideOutLeft {
  animation-name: slideOutLeft;
}
@keyframes slideOutRight {
  0% {
    transform: translateZ(0);
  }
  to {
    visibility: hidden;
    transform: translate3d(100%, 0, 0);
  }
}
.slideOutRight {
  animation-name: slideOutRight;
}
@keyframes slideOutUp {
  0% {
    transform: translateZ(0);
  }
  to {
    visibility: hidden;
    transform: translate3d(0, -100%, 0);
  }
}
.slideOutUp {
  animation-name: slideOutUp;
}

html {
  overflow-x: hidden;
}
body {
  background: #fff;
  color: #444;
  font-family: "Open Sans", sans-serif;
}

a {
  color: #007bff;
  transition: 0.5s;
}

a:hover,
a:active,
a:focus {
  color: #0b6bd3;
  outline: none;
  text-decoration: none;
}

p {
  padding: 0;
  margin: 0 0 30px 0;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  font-family: "Montserrat", sans-serif;
  font-weight: 400;
  margin: 0 0 20px 0;
  padding: 0;
}

/* Back to top button */

.back-to-top {
  position: fixed;
  display: none;
  background: #007bff;
  color: #fff;
  width: 44px;
  height: 44px;
  text-align: center;
  line-height: 1;
  font-size: 16px;
  border-radius: 50%;
  right: 15px;
  bottom: 15px;
  transition: background 0.5s;
  z-index: 11;
}

.back-to-top i {
  padding-top: 12px;
  color: #fff;
}

@-webkit-keyframes animate-preloader {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }

  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

@keyframes animate-preloader {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }

  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

.main-pages {
  margin-top: 60px;
}

.main-nav {
  /* Drop Down */
  /* Deep Drop Down */
}

.main-nav,
.main-nav * {
  margin: 0;
  padding: 0;
  list-style: none;
}

.main-nav > ul > li {
  position: relative;
  white-space: nowrap;
  float: left;
}

.main-nav a {
  display: block;
  position: relative;
  color: #004289;
  padding: 8px 20px;
  transition: 0.3s;
  font-size: 18px;
  font-family: "Montserrat", sans-serif;
  font-weight: 500;
}

.main-nav a:hover,
.main-nav .active > a,
.main-nav li:hover > a {
  color: #007bff;
  text-decoration: none;
}

.main-nav .drop-down ul {
  display: block;
  position: absolute;
  left: 0;
  top: calc(100% + 30px);
  z-index: 99;
  opacity: 0;
  visibility: hidden;
  padding: 10px 0;
  background: #fff;
  box-shadow: 0px 0px 30px rgba(127, 137, 161, 0.25);
  transition: ease all 0.3s;
}

.main-nav .drop-down:hover > ul {
  opacity: 1;
  top: 100%;
  visibility: visible;
}

.main-nav .drop-down li {
  min-width: 180px;
  position: relative;
}

.main-nav .drop-down ul a {
  padding: 10px 20px;
  font-size: 13px;
  color: #004289;
}

.main-nav .drop-down ul a:hover,
.main-nav .drop-down ul .active > a,
.main-nav .drop-down ul li:hover > a {
  color: #007bff;
}

.main-nav .drop-down > a:after {
  content: "\f107";
  font-family: FontAwesome;
  padding-left: 10px;
}

.main-nav .drop-down .drop-down ul {
  top: 0;
  left: calc(100% - 30px);
}

.main-nav .drop-down .drop-down:hover > ul {
  opacity: 1;
  top: 0;
  left: 100%;
}

.main-nav .drop-down .drop-down > a {
  padding-right: 35px;
}

.main-nav .drop-down .drop-down > a:after {
  content: "\f105";
  position: absolute;
  right: 15px;
}

/* Mobile Navigation */

.mobile-nav {
  position: fixed;
  top: 0;
  bottom: 0;
  z-index: 9999;
  overflow-y: auto;
  left: -260px;
  width: 260px;
  padding-top: 18px;
  background: rgba(19, 39, 57, 0.8);
  transition: 0.4s;
}

.mobile-nav * {
  margin: 0;
  padding: 0;
  list-style: none;
}

.mobile-nav a {
  display: block;
  position: relative;
  color: #fff;
  padding: 10px 20px;
  font-weight: 500;
}

.mobile-nav a:hover,
.mobile-nav .active > a,
.mobile-nav li:hover > a {
  color: #74b5fc;
  text-decoration: none;
}

.mobile-nav .drop-down > a:after {
  content: "\f078";
  font-family: FontAwesome;
  padding-left: 10px;
  position: absolute;
  right: 15px;
}

.mobile-nav .active.drop-down > a:after {
  content: "\f077";
}

.mobile-nav .drop-down > a {
  padding-right: 35px;
}

.mobile-nav .drop-down ul {
  display: none;
  overflow: hidden;
}

.mobile-nav .drop-down li {
  padding-left: 20px;
}

.mobile-nav-toggle {
  position: fixed;
  right: 0;
  top: 0;
  z-index: 9998;
  border: 0;
  background: none;
  font-size: 24px;
  transition: all 0.4s;
  outline: none !important;
  line-height: 1;
  cursor: pointer;
  text-align: right;
}

.mobile-nav-toggle i {
  margin: 18px 18px 0 0;
  color: #004289;
}

.mobile-nav-overly {
  width: 100%;
  height: 100%;
  z-index: 9997;
  top: 0;
  left: 0;
  position: fixed;
  background: rgba(19, 39, 57, 0.8);
  overflow: hidden;
  display: none;
}

.mobile-nav-active {
  overflow: hidden;
}

.mobile-nav-active .mobile-nav {
  left: 0;
}

.mobile-nav-active .mobile-nav-toggle i {
  color: #fff;
}

.section-header h3 {
  font-size: 36px;
  color: #283d50;
  text-align: center;
  font-weight: 500;
  position: relative;
}

.section-header p {
  text-align: center;
  margin: auto;
  font-size: 15px;
  padding-bottom: 60px;
  color: #556877;
  width: 50%;
}

.section-bg {
  background: #ecf5ff;
}

.icon {
  position: absolute;
  left: -10px;
  top: calc(50% - 32px);
}

.icon i {
  font-size: 64px;
  line-height: 1;
  transition: 0.5s;
}

.title {
  margin-left: 40px;
  font-weight: 700;
  margin-bottom: 15px;
  font-size: 18px;
}

.title a {
  color: #111;
}

.box:hover .title a {
  color: #007bff;
}

.description {
  font-size: 14px;
  margin-left: 0px;
  margin-top: 10px;
  line-height: 24px;
  margin-bottom: 0;
}

.btn6-get-started,
.btn6-services {
  font-family: "Montserrat", sans-serif;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 1px;
  display: inline-block;
  padding: 10px 32px;
  border-radius: 50px;
  transition: 0.5s;
  margin: 0 20px 20px 0;
  color: #fff;
}

.btn6-get-started {
  background: #007bff;
  border: 2px solid #007bff;
  color: #fff;
}

.btn6-get-started:hover {
  background: none;
  border-color: #007bff;
  color: #007bff;
}

.btn6-services {
  border: 2px solid #007bff;
}

.btn6-services:hover {
  background: #007bff;
  border-color: #007bff;
  color: #007bff;
}

.box {
  padding: 50px;
  position: relative;
  overflow: hidden;
  border-radius: 10px;
  margin: 20px 10px 40px 10px;
  background: #fff;
  box-shadow: 0 10px 29px 0 rgba(68, 88, 144, 0.1);
  transition: all 0.3s ease-in-out;
}

.box:hover {
  -webkit-transform: translateY(-5px);
  transform: translateY(-5px);
}

.bttn-unite {
  margin-left: 60px;
  margin-top: 58px;
  color: #0d61fe;
  border-color: transparent;
  background: transparent;
  cursor: pointer;
  position: relative;
  font-size: 20px;
  font-family: inherit;
  padding: 5px 20px;
  overflow: hidden;
  border: 3px solid #0d61fe;
  border-radius: 100px;
  background: #fff;
  color: #0d61fe;
  -webkit-transition: color 0.3s cubic-bezier(0.02, 0.01, 0.47, 1),
    border-color 0.3s cubic-bezier(0.02, 0.01, 0.47, 1);
  transition: color 0.3s cubic-bezier(0.02, 0.01, 0.47, 1),
    border-color 0.3s cubic-bezier(0.02, 0.01, 0.47, 1);
}
.bttn-unite:before {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 120%;
  background: #d6e3ff;
  content: "";
  opacity: 0;
  z-index: -1;
  -webkit-transition: opacity 0.15s cubic-bezier(0.02, 0.01, 0.47, 1),
    -webkit-transform 0.15s cubic-bezier(0.02, 0.01, 0.47, 1);
  transition: opacity 0.15s cubic-bezier(0.02, 0.01, 0.47, 1),
    -webkit-transform 0.15s cubic-bezier(0.02, 0.01, 0.47, 1);
  transition: transform 0.15s cubic-bezier(0.02, 0.01, 0.47, 1),
    opacity 0.15s cubic-bezier(0.02, 0.01, 0.47, 1);
  transition: transform 0.15s cubic-bezier(0.02, 0.01, 0.47, 1),
    opacity 0.15s cubic-bezier(0.02, 0.01, 0.47, 1),
    -webkit-transform 0.15s cubic-bezier(0.02, 0.01, 0.47, 1);
  -webkit-transform: translate3d(-110%, -10%, 0) skewX(-20deg);
  transform: translate3d(-110%, -10%, 0) skewX(-20deg);
}
.bttn-unite:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 120%;
  background: rgba(214, 227, 255, 0.7);
  content: "";
  opacity: 0;
  z-index: -1;
  -webkit-transition: opacity 0.15s cubic-bezier(0.02, 0.01, 0.47, 1),
    -webkit-transform 0.15s cubic-bezier(0.02, 0.01, 0.47, 1);
  transition: opacity 0.15s cubic-bezier(0.02, 0.01, 0.47, 1),
    -webkit-transform 0.15s cubic-bezier(0.02, 0.01, 0.47, 1);
  transition: transform 0.15s cubic-bezier(0.02, 0.01, 0.47, 1),
    opacity 0.15s cubic-bezier(0.02, 0.01, 0.47, 1);
  transition: transform 0.15s cubic-bezier(0.02, 0.01, 0.47, 1),
    opacity 0.15s cubic-bezier(0.02, 0.01, 0.47, 1),
    -webkit-transform 0.15s cubic-bezier(0.02, 0.01, 0.47, 1);
  -webkit-transform: translate3d(110%, -10%, 0) skewX(-20deg);
  transform: translate3d(110%, -10%, 0) skewX(-20deg);
}
</style>
