<template>
  <q-page class="flex flex-direction-vertical">
    <div class="main">
      <q-card class="dialog-custom-card-container-new">
        <q-card-section class="row flex flex-center dialog-switch-card-title">
          <div class="text-h6" style="position: relative; top: 25px">
            自定义切换策略
          </div>
        </q-card-section>
        <div v-show="member_mismatch" style="margin-top: 30px">
          <span style="color: #ed6563"
            >请保证小组成员至少有一名为高开放性、高宜人性人格！</span
          >
        </div>
        <q-card-section>
          <div
            class="row dialog-switch-card-content1-line1"
            style="position: absolute; top: 50px; margin-left: 20px"
          >
            <div
              class="text-subtitle1 flex flex-left dialog-custom-card-content1-title"
            >
              成员1信息
            </div>
            <div
              class="flex flex-direction-horizontal"
              style="
                justify-content: space-between;
                margin-bottom: 10px;
                margin-left: -28px;
              "
            >
              <div
                style="
                  color: #0d2436;
                  font-size: 14px;
                  margin-left: 0px;
                  height: 30px;
                "
              >
                开放性
              </div>
              <select
                name="status"
                id="status"
                v-model="open_1"
                style="font-size: 14px; width: 80px"
              >
                <option value="1">低(0-12)</option>
                <option value="2">中(12-24)</option>
                <option value="3">高(>24)</option>
              </select>
              <div style="color: #0d2436; font-size: 14px; margin-left: 6px">
                外向性
              </div>
              <select
                name="status"
                id="status"
                v-model="outgoing_1"
                style="font-size: 14px; width: 80px"
              >
                <option value="1">低(0-12)</option>
                <option value="2">中(12-24)</option>
                <option value="3">高(>24)</option>
              </select>
              <div style="color: #0d2436; font-size: 14px; margin-left: 6px">
                责任性
              </div>
              <select
                name="status"
                id="status"
                v-model="responsibility_1"
                style="font-size: 14px; width: 80px"
              >
                <option value="1">低(0-12)</option>
                <option value="2">中(12-24)</option>
                <option value="3">高(>24)</option>
              </select>
              <div style="color: #0d2436; font-size: 14px; margin-left: 6px">
                宜人性
              </div>
              <select
                name="status"
                id="status"
                v-model="pleasant_1"
                style="font-size: 14px; width: 80px"
              >
                <option value="1">低(0-12)</option>
                <option value="2">中(12-24)</option>
                <option value="3">高(>24)</option>
              </select>
              <div style="color: #0d2436; font-size: 14px; margin-left: 6px">
                神经质
              </div>
              <select
                name="status"
                id="status"
                v-model="nerve_1"
                style="font-size: 14px; width: 80px"
              >
                <option value="1">低(0-12)</option>
                <option value="2">中(12-24)</option>
                <option value="3">高(>24)</option>
              </select>
            </div>
            <div
              class="text-subtitle1 flex flex-left dialog-custom-card-content1-title"
            >
              成员2信息
            </div>
            <div
              class="flex flex-direction-horizontal"
              style="
                justify-content: space-between;
                margin-bottom: 10px;
                margin-left: -28px;
              "
            >
              <div
                style="
                  color: #0d2436;
                  font-size: 14px;
                  margin-left: 0px;
                  height: 30px;
                "
              >
                开放性
              </div>
              <select
                name="status"
                id="status"
                v-model="open_2"
                style="font-size: 14px; width: 80px"
              >
                <option value="1">低(0-12)</option>
                <option value="2">中(12-24)</option>
                <option value="3">高(>24)</option>
              </select>
              <div style="color: #0d2436; font-size: 14px; margin-left: 6px">
                外向性
              </div>
              <select
                name="status"
                id="status"
                v-model="outgoing_2"
                style="font-size: 14px; width: 80px"
              >
                <option value="1">低(0-12)</option>
                <option value="2">中(12-24)</option>
                <option value="3">高(>24)</option>
              </select>
              <div style="color: #0d2436; font-size: 14px; margin-left: 6px">
                责任性
              </div>
              <select
                name="status"
                id="status"
                v-model="responsibility_2"
                style="font-size: 14px; width: 80px"
              >
                <option value="1">低(0-12)</option>
                <option value="2">中(12-24)</option>
                <option value="3">高(>24)</option>
              </select>
              <div style="color: #0d2436; font-size: 14px; margin-left: 6px">
                宜人性
              </div>
              <select
                name="status"
                id="status"
                v-model="pleasant_2"
                style="font-size: 14px; width: 80px"
              >
                <option value="1">低(0-12)</option>
                <option value="2">中(12-24)</option>
                <option value="3">高(>24)</option>
              </select>
              <div style="color: #0d2436; font-size: 14px; margin-left: 6px">
                神经质
              </div>
              <select
                name="status"
                id="status"
                v-model="nerve_2"
                style="font-size: 14px; width: 80px"
              >
                <option value="1">低(0-12)</option>
                <option value="2">中(12-24)</option>
                <option value="3">高(>24)</option>
              </select>
            </div>
            <div
              class="text-subtitle1 flex flex-left dialog-custom-card-content1-title"
            >
              成员3信息
            </div>
            <div
              class="flex flex-direction-horizontal"
              style="
                justify-content: space-between;
                margin-bottom: 10px;
                margin-left: -28px;
              "
            >
              <div
                style="
                  color: #0d2436;
                  font-size: 14px;
                  margin-left: 0px;
                  height: 30px;
                "
              >
                开放性
              </div>
              <select
                name="status"
                id="status"
                v-model="open_3"
                style="font-size: 14px; width: 80px"
              >
                <option value="1">低(0-12)</option>
                <option value="2">中(12-24)</option>
                <option value="3">高(>24)</option>
              </select>
              <div style="color: #0d2436; font-size: 14px; margin-left: 6px">
                外向性
              </div>
              <select
                name="status"
                id="status"
                v-model="outgoing_3"
                style="font-size: 14px; width: 80px"
              >
                <option value="1">低(0-12)</option>
                <option value="2">中(12-24)</option>
                <option value="3">高(>24)</option>
              </select>
              <div style="color: #0d2436; font-size: 14px; margin-left: 6px">
                责任性
              </div>
              <select
                name="status"
                id="status"
                v-model="responsibility_3"
                style="font-size: 14px; width: 80px"
              >
                <option value="1">低(0-12)</option>
                <option value="2">中(12-24)</option>
                <option value="3">高(>24)</option>
              </select>
              <div style="color: #0d2436; font-size: 14px; margin-left: 6px">
                宜人性
              </div>
              <select
                name="status"
                id="status"
                v-model="pleasant_3"
                style="font-size: 14px; width: 80px"
              >
                <option value="1">低(0-12)</option>
                <option value="2">中(12-24)</option>
                <option value="3">高(>24)</option>
              </select>
              <div style="color: #0d2436; font-size: 14px; margin-left: 6px">
                神经质
              </div>
              <select
                name="status"
                id="status"
                v-model="nerve_3"
                style="font-size: 14px; width: 80px"
              >
                <option value="1">低(0-12)</option>
                <option value="2">中(12-24)</option>
                <option value="3">高(>24)</option>
              </select>
            </div>
          </div>
          <div
            class="flex flex-direction-horizontal"
            style="
              margin-left: 460px;
              padding-top: 40px;
              margin-top: 90px;
              margin-bottom: 20px;
            "
          >
            <q-btn
              unelevated
              rounded
              label="Cancle"
              @click="this.$router.push('/usage')"
              style="margin-right: 20px"
              class="bttn-unite"
            />
            <!-- @click="" -->
            <q-btn
              unelevated
              rounded
              label="Start"
              @click="onCheckMemberMatch"
              class="button-begin"
            />
          </div>
        </q-card-section>
      </q-card>
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  data() {
    return {
      open_1: "",
      outgoing_1: "",
      responsibility_1: "",
      pleasant_1: "",
      nerve_1: "",
      open_2: "",
      outgoing_2: "",
      responsibility_2: "",
      pleasant_2: "",
      nerve_2: "",
      open_3: "",
      outgoing_3: "",
      responsibility_3: "",
      pleasant_3: "",
      nerve_3: "",
      member_mismatch: false,
    };
  },
  methods: {
    // 判断成员匹配程度
    onCheckMemberMatch() {
      if (
        (this.open_1 == "3" || this.open_2 == "3" || this.open_3 == "3") &&
        (this.pleasant_1 == "3" ||
          this.pleasant_2 == "3" ||
          this.pleasant_3 == "3")
      ) {
        this.member_mismatch = false;
        this.$router.push("/discuss");
      } else {
        this.member_mismatch = true;
      }
    },
  },
});
</script>

<style lang="scss" scoped>
.switch-title {
  margin-top: 16px;
  margin-left: 32px;
}

.switch-container {
  margin-top: 16px;
  margin-right: 32px;
  margin-left: 32px;
  height: 200px;
  background: #192431;
  border-radius: 20px;
}

.switch-item-container {
  width: 240px;
}

.switch-item-box-container {
  width: 100%;
  margin-left: 16px;
  margin-right: 16px;
  height: 160px;
  background: #222041;
  border-radius: 10px;
}

.switch-item-icon {
  height: 80px;
  width: 80px;
}

.switch-item-text {
  margin-top: 8px;
}

.dialog-switch-card-container {
  background-color: #081420;
  width: 480px;
}

.dialog-custom-card-container {
  background-color: #ffffff;
  max-width: 640px;
}

.dialog-switch-close-button-container {
  justify-content: end;
  padding-bottom: 0;
}

.dialog-switch-card-title {
  padding-top: 0;
  padding-bottom: 0;
}

.dialog-switch-spilt-line {
  margin-top: 10px;
  margin-bottom: 10px;
  border-top: 2px solid #fbfbfb;
}

.dialog-switch-card-content1 {
  padding-bottom: 0;
}

.dialog-switch-card-content1-line1 {
  height: 50px;
}

.dialog-custom-card-content1-line1 {
  padding-top: 8px;
  height: 32px;
}

.dialog-switch-card-content1-line2 {
  height: 32px;
}

.dialog-custom-card-content1-line2 {
  padding-top: 8px;
  height: 32px;
}

.dialog-switch-card-content2 {
  height: 40px;
}

.dialog-switch-card-content1-title {
  width: 81px;
}

.dialog-custom-card-content1-title {
  width: 120px;
}

.dialog-switch-card-content3 {
  margin-right: 16px;
  justify-content: space-around;
  height: 32px;
  margin-top: 8px;
  margin-bottom: 24px;
}

.dialog-switch-card-content3-spilt-line {
  margin: 8px;
  border-right: 2px solid #fbfbfb;
}

.dialog-switch-card-content4 {
  padding-top: 0;
}

.dialog-switch-card-content4-button {
  padding: 8px 32px;
}

.text-dialog {
  color: #192030;
  font-size: 20px;
  font-weight: 400;
}

.select-style {
  background-color: rgba(0, 0, 0, 0.2) !important;
  border: 1px solid #15285b !important;
  color: #ffffff !important;
  font-size: 12px;
}

.dialog-custom-card-container-new {
  width: 800px;
  height: 300px;
  border-radius: 10px;
  box-shadow: 0 10px 29px 0 rgba(68, 88, 144, 0.1);
}

.flex-direction-horizontal {
  flex-direction: row;
}

.button-begin {
  margin-top: 58px;
  padding: 8px 32px 8px 32px;
  color: white;
  font-size: 16px;
  background-color: #0d61fe;
}

.main {
  text-align: center;
  background-color: #fff;
  border-radius: 10px;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
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

.bttn-unite {
  margin-left: 60px;
  margin-top: 58px;
  border-color: transparent;
  background: transparent;
  cursor: pointer;
  position: relative;
  font-size: 16px;
  font-family: inherit;
  padding: 5px 25px;
  overflow: hidden;
  border: 2px solid #0d61fe;
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
