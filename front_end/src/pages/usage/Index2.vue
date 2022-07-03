<template>
  <q-page class="flex flex-direction-vertical">
    <div>
      <div class="text-h6 switch-title">自定义策略</div>
      <!--      <div-->
      <!--        class="flex flex-center-vertical flex-direction-horizontal switch-container"-->
      <!--      >-->
      <!--        <q-btn-->
      <!--          flat-->
      <!--          class="flex flex-direction-vertical switch-item-container"-->
      <!--          @click="showModel2"-->
      <!--        >-->
      <!--          <div class="flex flex-center switch-item-box-container">-->
      <!--            <q-icon name="add" />-->
      <!--          </div>-->
      <!--          <div class="text-center text-subtitle2 switch-item-text">-->
      <!--            添加新的切换策略-->
      <!--          </div>-->
      <!--        </q-btn>-->
      <!--      </div>-->
    </div>
    <q-dialog v-model="model2" class="text-white" persistent>
      <q-card class="dialog-custom-card-container">
        <q-card-section class="flex dialog-switch-close-button-container">
          <q-btn icon="close" flat round dense v-close-popup />
        </q-card-section>
        <q-card-section class="row flex flex-center dialog-switch-card-title">
          <div class="text-h6">自定义切换策略</div>
        </q-card-section>
        <q-card-section>
          <div class="row dialog-switch-card-content1-line1">
            <div class="flex flex-center dialog-custom-card-content1-title">
              选择切换维度：
            </div>
            <div
              class="flex flex-direction-horizontal"
              style="justify-content: space-between"
            >
              <q-radio dark v-model="mode2" val="1" label="现在和未来场景" />
              <q-radio dark v-model="mode2" val="2" label="类比任务的内容" />
              <q-radio
                dark
                v-model="mode2"
                val="3"
                label="构思任务和类比任务"
              />
            </div>
          </div>
        </q-card-section>
        <q-card-section class="dialog-switch-card-content1">
          <div class="text-subtitle2">设置时间模式</div>
          <div class="row dialog-custom-card-content1-line1">
            <div
              class="flex flex-center-vertical dialog-switch-card-content1-title"
            >
              总时长：
            </div>
            <div
              class="flex flex-direction-horizontal"
              style="justify-content: space-between"
            >
              <q-radio dark v-model="mode3" val="1" label="30分钟" />
              <q-radio dark v-model="mode3" val="2" label="45分钟" />
              <q-radio dark v-model="mode3" val="3" label="60分钟" />
              <q-radio dark v-model="mode3" val="4" label="90分钟" />
              <q-radio dark v-model="mode3" val="5">
                <q-input
                  style="margin-left: 20px; width: 80px; max-width: 80px"
                  dark
                  label="输入时长"
                />
              </q-radio>
            </div>
          </div>
          <div
            class="row dialog-custom-card-content1-line2"
            style="margin-top: 24px"
          >
            <div
              class="flex flex-center-vertical dialog-switch-card-content1-title"
            >
              轮次：
            </div>
            <div class="flex flex-direction-horizontal">
              <q-input
                v-model="times"
                style="width: 40px; max-width: 40px"
                dark
              />
              <div class="flex flex-center-vertical">次</div>
            </div>
          </div>
          <div class="row" style="margin-top: 48px">
            <div class="flex flex-center dialog-switch-card-content2">
              分配模式：
            </div>
            <div class="flex flex-direction-horizontal">
              <q-radio dark v-model="mode4" val="1">
                <div>平均分配</div>
                <div>（每段讨论时间相等）</div>
              </q-radio>
              <q-radio dark v-model="mode4" val="2">
                <div>递减分配</div>
                <div>（每段讨论时间逐渐减少）</div>
              </q-radio>
            </div>
          </div>
          <div
            class="row flex dialog-switch-card-content3"
            style="margin-top: 24px"
          >
            <div class="dialog-custom-card-content1-title">生成进度预览：</div>
            <div class="flex flex-direction-vertical">
              <div>任务A</div>
              <div>20</div>
            </div>
            <div class="dialog-switch-card-content3-spilt-line" />
            <div class="flex flex-direction-vertical">
              <div>任务A</div>
              <div>20</div>
            </div>
            <div class="dialog-switch-card-content3-spilt-line" />
            <div class="flex flex-direction-vertical">
              <div>任务A</div>
              <div>20</div>
            </div>
            <div class="dialog-switch-card-content3-spilt-line" />
            <div class="flex flex-direction-vertical">
              <div>任务A</div>
              <div>20</div>
            </div>
            <div class="dialog-switch-card-content3-spilt-line" />
            <div class="flex flex-direction-vertical">
              <div>任务A</div>
              <div>20</div>
            </div>
            <div class="dialog-switch-card-content3-spilt-line" />
            <div class="flex flex-direction-vertical">
              <div>任务A</div>
              <div>20</div>
            </div>
          </div>
          <div class="dialog-switch-spilt-line" />
        </q-card-section>
        <q-card-actions align="right" class="dialog-switch-card-content4">
          <q-btn
            unelevated
            rounded
            color="pink"
            disable
            label="保存"
            size="12px"
            class="dialog-switch-card-content4-button"
          />
          <q-btn
            unelevated
            rounded
            color="pink"
            @click="this.$router.push('/discuss')"
            :disable="
              mode2 !== '1' || mode3 !== '4' || times !== '6' || mode4 !== '2'
            "
            label="保存并创建讨论"
            size="12px"
            class="dialog-switch-card-content4-button"
          />
        </q-card-actions>
      </q-card>
    </q-dialog>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "PageIndex",
  data: () => ({
    model1: false,
    model2: false,
    mode: "2",
    mode2: "1",
    times: "6",
    mode3: "4",
    mode4: "2",
  }),
  methods: {
    showModel1() {
      this.model1 = true;
    },
    showModel2() {
      this.model2 = true;
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
  background-color: #081420;
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
  height: 32px;
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
  width: 98px;
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
</style>
