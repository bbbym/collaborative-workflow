<template>
  <q-page class="flex flex-direction-vertical">
    <div>
      <div class="text-h6 switch-title">我的讨论</div>
      <div
        class="flex flex-center-vertical flex-direction-horizontal switch-container"
      >
        <q-btn
          flat
          class="flex flex-direction-vertical switch-item-container"
          @click="showModel2"
        >
          <div class="flex flex-center switch-item-box-container">
            <q-icon name="add" />
          </div>
        </q-btn>
      </div>
    </div>
    <q-dialog v-model="model2" class="text-white">
      <q-card class="dialog-custom-card-container">
        <q-card-section class="row bg-tab padding-zero">
          <q-tabs v-model="tab" class="flex tab-container">
            <!--            <q-tab name="switch" label="自定义切换策略" />-->
            <q-tab name="custom" label="自定义切换策略" />
          </q-tabs>
        </q-card-section>
        <q-card-section>
          <q-tab-panels v-model="tab" animated class="model-background">
            <!--            <q-tab-panel name="switch" class="padding-zero">-->
            <!--              <div class="flex dialog-switch-card-content switch-container">-->
            <!--                <q-btn-->
            <!--                  flat-->
            <!--                  @click="this.$router.push('/discuss')"-->
            <!--                  class="flex flex-direction-vertical switch-item-container"-->
            <!--                >-->
            <!--                  <div class="flex flex-center switch-item-box-container">-->
            <!--                    <q-img-->
            <!--                      src="../../assets/img5.png"-->
            <!--                      class="switch-item-icon"-->
            <!--                    />-->
            <!--                  </div>-->
            <!--                  <div class="text-center text-subtitle switch-item-text">-->
            <!--                    服务设计概念衍生-->
            <!--                  </div>-->
            <!--                </q-btn>-->
            <!--                <q-btn-->
            <!--                  flat-->
            <!--                  class="flex flex-direction-vertical switch-item-container"-->
            <!--                >-->
            <!--                  <div class="flex flex-center switch-item-box-container">-->
            <!--                    <q-img-->
            <!--                      src="../../assets/img_empty.png"-->
            <!--                      class="switch-item-icon"-->
            <!--                    />-->
            <!--                  </div>-->
            <!--                  <div class="text-center text-subtitle2 switch-item-text">-->
            <!--                    功能即将上线-->
            <!--                  </div>-->
            <!--                </q-btn>-->
            <!--                <q-btn-->
            <!--                  flat-->
            <!--                  class="flex flex-direction-vertical switch-item-container"-->
            <!--                >-->
            <!--                  <div class="flex flex-center switch-item-box-container">-->
            <!--                    <q-img-->
            <!--                      src="../../assets/img_empty.png"-->
            <!--                      class="switch-item-icon"-->
            <!--                    />-->
            <!--                  </div>-->
            <!--                  <div class="text-center text-subtitle2 switch-item-text">-->
            <!--                    功能即将上线-->
            <!--                  </div>-->
            <!--                </q-btn>-->
            <!--              </div>-->
            <!--            </q-tab-panel>-->
            <q-tab-panel name="custom" class="padding-zero">
              <q-card-section>
                <div class="row dialog-switch-card-content1-line1">
                  <div
                    class="flex flex-center dialog-custom-card-content1-title"
                  >
                    选择切换维度：
                  </div>
                  <div
                    class="flex flex-direction-horizontal dialog-custom-card-content1-container"
                  >
                    <q-radio
                      dark
                      v-model="mode2"
                      val="1"
                      label="现在和未来场景"
                    />
                    <q-radio
                      dark
                      v-model="mode2"
                      val="2"
                      label="类比任务的内容"
                    />
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
                    class="flex flex-direction-horizontal dialog-custom-card-content1-container"
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
                  class="row dialog-custom-card-content1-line2 margin-top-24"
                >
                  <div
                    class="flex flex-center-vertical dialog-switch-card-content1-title"
                  >
                    轮次：
                  </div>
                  <div class="flex flex-direction-horizontal">
                    <q-input
                      v-model="times"
                      dark
                      class="dialog-custom-card-content1-line2-input"
                    />
                    <div class="flex flex-center-vertical">次</div>
                  </div>
                </div>
                <div class="row margin-top-48">
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
                <div class="row flex dialog-switch-card-content3 margin-top-24">
                  <div class="dialog-custom-card-content1-title">
                    生成进度预览：
                  </div>
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
                    mode2 !== '1' ||
                    mode3 !== '4' ||
                    times !== '6' ||
                    mode4 !== '2'
                  "
                  label="保存并创建讨论"
                  size="12px"
                  class="dialog-switch-card-content4-button"
                />
              </q-card-actions>
            </q-tab-panel>
          </q-tab-panels>
        </q-card-section>
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
    mode2: "1",
    times: "6",
    mode3: "4",
    mode4: "2",
    tab: "switch",
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

.dialog-custom-card-container {
  background-color: #ffffff;
  max-width: 800px;
  width: 540px;
  border-radius: 12px;
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

.padding-zero {
  padding: 0;
}

.model-background {
  background-color: #ffffff;
  box-shadow: 0 10px 29px 0 rgba(68, 88, 144, 0.1);
}

.tab-container {
  justify-content: space-between;
  width: 100%;
}

.switch-container1 {
  justify-content: space-between;
  flex-wrap: wrap;
}

.dialog-custom-card-content1-container {
  justify-content: space-between;
}

.dialog-custom-card-content1-input {
  margin-left: 20px;
  width: 80px;
  max-width: 80px;
}

.margin-top-24 {
  margin-top: 24px;
}

.dialog-custom-card-content1-line2-input {
  width: 40px;
  max-width: 40px;
}

.margin-top-48 {
  margin-top: 48px;
}
</style>
