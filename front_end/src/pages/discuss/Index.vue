<template>
  <q-page class="flex flex-direction-vertical" style="min-height: 0">
    <div class="row">
      <div class="col-6">
        <div
          class="q-pb-md q-px-lg q-mx-96 box-container"
          v-show="timer.index == 0"
          style="
            position: absolute;
            left: 780px;
            top: 160px;
            height: 500px;
            width: 550px;
          "
        >
          <div class="row flex-center q-pa-lg">
            <div class="flex flex-center" style="color: #0d2436">
              第一轮 设计问题发散阶段
            </div>
            <q-linear-progress
              rounded
              white
              size="8px"
              :value="0.16"
              class="box-progress-bar"
            />
          </div>
          <div class="row flex-center" style="margin-top: 30px">
            <div
              class="flex flex-center text-center bg-color-0D61FE box-item-mz"
              style="color: #1d1d1d"
            >
              要保证一定的互动次数，对设计问题进行深入挖掘，对设计情景进行全面讨论，发现更多设计机会。
            </div>
            <div
              class="flex flex-center text-center bg-color-3CE8C1 box-item-md q-ml-8"
              style="color: #1d1d1d"
            >
              没有想法时，可以通过长时间的静默思考沉淀想法，再开启一段良好的互动。
            </div>
            <div
              class="flex flex-center text-center bg-color-3CE8C1 box-item-sm q-ml-8"
              style="color: #1d1d1d"
            >
              分享信息时要简短快速，给别人留出思考和补充的空间。
            </div>
            <div
              class="flex flex-center text-center bg-color-5B58F4 box-item-sm q-ml-8"
              style="color: #1d1d1d"
            >
              ① 总结他人说过的话，聚焦关键信息.
            </div>
            <div
              class="flex flex-center text-center bg-color-5B58F4 box-item-md"
              style="color: #1d1d1d"
            >
              ② 联想与他人提供信息相关的事件、新闻、经历、观点等。
            </div>
            <div
              class="flex flex-center text-center bg-color-5B58F4 box-item-sm q-ml-8"
              style="color: #1d1d1d"
            >
              ③ 优先关注主要问题，而非细节问题。
            </div>
            <div
              class="flex flex-center text-center bg-color-5B58F4 box-item-sm q-ml-8"
              style="color: #1d1d1d"
            >
              ④ 允许每个设计方向都得到充分讨论。
            </div>
          </div>
          <div class="row flex-center q-mt-8"></div>
        </div>
        <div
          class="q-pb-md q-px-lg q-mx-96 box-container"
          v-show="timer.index == 1"
          style="
            position: absolute;
            left: 780px;
            top: 160px;
            height: 500px;
            width: 550px;
          "
        >
          <div class="row flex-center q-pa-lg">
            <div class="flex flex-center" style="color: #0d2436">
              第二轮 设计问题收敛阶段
            </div>
            <q-linear-progress
              rounded
              white
              size="8px"
              :value="0.16"
              class="box-progress-bar"
            />
          </div>
          <div class="row flex-center" style="margin-top: 30px">
            <div
              class="flex flex-center text-center bg-color-0D61FE box-item-mz"
              style="color: #1d1d1d"
            >
              不必追求均衡的个人发言时间。
            </div>
            <div
              class="flex flex-center text-center bg-color-5B58F4 box-item-sm q-ml-8"
              style="color: #1d1d1d"
            >
              ① 聚焦的需求是否可以通过设计的方式解决？
            </div>
            <div
              class="flex flex-center text-center bg-color-5B58F4 box-item-md"
              style="color: #1d1d1d"
            >
              ② 有多少用户有这个需求？他们的需求程度一样吗？
            </div>
            <div
              class="flex flex-center text-center bg-color-5B58F4 box-item-sm q-ml-8"
              style="color: #1d1d1d"
            >
              ③ 这个需求是在特定情境下才会发生的极少数需求吗？
            </div>
            <div
              class="flex flex-center text-center bg-color-5B58F4 box-item-sm q-ml-8"
              style="color: #1d1d1d"
            >
              ④ 这个需求在实际生活中是急需解决的吗？
            </div>
          </div>
          <div class="row flex-center q-mt-8"></div>
        </div>
        <div
          class="q-pb-md q-px-lg q-mx-96 box-container"
          v-show="timer.index == 2"
          style="
            position: absolute;
            left: 780px;
            top: 160px;
            height: 500px;
            width: 550px;
          "
        >
          <div class="row flex-center q-pa-lg">
            <div class="flex flex-center" style="color: #0d2436">
              第三轮 设计方案发散阶段
            </div>
            <q-linear-progress
              rounded
              white
              size="8px"
              :value="0.16"
              class="box-progress-bar"
            />
          </div>
          <div class="row flex-center" style="margin-top: 30px">
            <div
              class="flex flex-center text-center bg-color-0D61FE box-item-mz"
              style="color: #1d1d1d"
            >
              不必追求均衡的个人发言时间。
            </div>
            <div
              class="flex flex-center text-center bg-color-3CE8C1 box-item-mz"
              style="color: #1d1d1d"
            >
              可以以一个人提出的方案生长为中心，其他人为该方案增加补充细节或删除不合理的部分。
            </div>
          </div>
          <div class="row flex-center q-mt-8"></div>
        </div>
        <div
          class="q-pb-md q-px-lg q-mx-96 box-container"
          v-show="timer.index == 3"
          style="
            position: absolute;
            left: 780px;
            top: 160px;
            height: 500px;
            width: 550px;
          "
        >
          <div class="row flex-center q-pa-lg">
            <div class="flex flex-center" style="color: #0d2436">
              第四阶段 设计方案收敛阶段
            </div>
            <q-linear-progress
              rounded
              white
              size="8px"
              :value="0.16"
              class="box-progress-bar"
            />
          </div>
          <div class="row flex-center" style="margin-top: 30px">
            <div
              class="flex flex-center text-center bg-color-0D61FE box-item-mz"
              style="color: #1d1d1d"
            >
              抓紧最后的讨论时间，减少方案不符合逻辑或难以实现的部分。
            </div>
            <div
              class="flex flex-center text-center bg-color-3CE8C1 box-item-md q-ml-8"
              style="color: #1d1d1d"
            >
              可以适当的进行独立思考。
            </div>
            <div
              class="flex flex-center text-center bg-color-5B58F4 box-item-sm q-ml-8"
              style="color: #1d1d1d"
            >
              ① 通过模拟用户的体验过程寻找漏洞.
            </div>
            <div
              class="flex flex-center text-center bg-color-5B58F4 box-item-md"
              style="color: #1d1d1d"
            >
              ② 从用户角度来说，他们使用服务的动机是否充分？
            </div>
            <div
              class="flex flex-center text-center bg-color-5B58F4 box-item-sm q-ml-8"
              style="color: #1d1d1d"
            >
              ③ 方案是否给其他利益相关者造成了困扰？
            </div>
            <div
              class="flex flex-center text-center bg-color-5B58F4 box-item-sm q-ml-8"
              style="color: #1d1d1d"
            >
              ④ 方案的商业模式是否合理？
            </div>
          </div>
          <div class="row flex-center q-mt-8"></div>
        </div>
<!--        <div-->
<!--          class="q-pb-md q-px-lg q-mx-96 box-container q-mt-md"-->
<!--          v-show="timer.index == 4"-->
<!--        >-->
<!--          <div class="row flex-center q-pa-lg">-->
<!--            <div class="flex flex-center">第五轮 对当下场景进行设计</div>-->
<!--            <q-linear-progress-->
<!--              rounded-->
<!--              dark-->
<!--              size="8px"-->
<!--              :value="0.83"-->
<!--              color="pink"-->
<!--              class="box-progress-bar"-->
<!--            />-->
<!--          </div>-->
<!--          <div class="row flex-center">-->
<!--            <div class="flex flex-direction-horizontal">-->
<!--              <div-->
<!--                class="flex flex-center text-center bg-color-6001D3 box-item-sm"-->
<!--              >-->
<!--                宣传方式的共性和同质化现象在消磨合作关系。-->
<!--              </div>-->
<!--              <div-->
<!--                class="flex flex-center text-center bg-color-6001D3 box-item-md q-ml-8"-->
<!--              >-->
<!--                信任危机正在慢慢蚕食优秀的探店达人积累的口碑，甚至影响到整个探店垂类内容的发展。-->
<!--              </div>-->
<!--              <div-->
<!--                class="flex flex-center text-center bg-color-FD346E box-item-md q-ml-8"-->
<!--              >-->
<!--                如今各类探店内容层出不穷，“特别乌啦啦”、“真探唐仁杰”等知名探店达人凭借自己的个人魅力深受粉丝的喜爱。-->
<!--              </div>-->
<!--            </div>-->
<!--            <div class="flex flex-direction-horizontal q-mt-8">-->
<!--              <div-->
<!--                class="flex flex-center text-center bg-color-FD346E box-item-md"-->
<!--              >-->
<!--                说清自己的喜好，讲清真实的感受，才能给消费者提供有价值的内容。-->
<!--              </div>-->
<!--              <div-->
<!--                class="flex flex-center text-center bg-color-6001D3 box-item-sm q-ml-8"-->
<!--              >-->
<!--                “探店博主培训”<br />-->
<!--                “五天带你成为探店博主”-->
<!--              </div>-->
<!--              <div-->
<!--                class="flex flex-center text-center bg-color-6001D3 box-item-md q-ml-8"-->
<!--              >-->
<!--                探店视频受到商业化的裹挟与影响，内容的真实性受到质疑。信任感受到了极大的挑战。-->
<!--              </div>-->
<!--            </div>-->
<!--          </div>-->
<!--        </div>-->
<!--        <div-->
<!--          class="q-pb-md q-px-lg q-mx-96 box-container q-mt-md q-mb-lg"-->
<!--          v-show="timer.index == 5"-->
<!--        >-->
<!--          <div class="row flex-center q-pa-lg">-->
<!--            <div class="flex flex-center">第六轮 对未来场景进行设计</div>-->
<!--            <q-linear-progress-->
<!--              rounded-->
<!--              dark-->
<!--              size="8px"-->
<!--              :value="1"-->
<!--              color="tab"-->
<!--              class="box-progress-bar"-->
<!--            />-->
<!--          </div>-->
<!--          <div class="row flex-center">-->
<!--            <div class="flex flex-direction-horizontal">-->
<!--              <div-->
<!--                class="flex flex-center text-center bg-color-6001D3 box-item-xl"-->
<!--              >-->
<!--                探店达人的商业模式通常分为两种：<br />-->
<!--                1.商家为达人提供免费的产品和服务，达人体验过后发布自己的感受与看法，这相当于一种资源置换；<br />-->
<!--                2.商家向达人本人支付推广费用，达人根据要求设置拍摄内容和推广方向，更像是一种商业合作。。-->
<!--              </div>-->
<!--              <div class="flex flex-direction-vertical q-ml-8">-->
<!--                <div class="flex flex-direction-horizontal">-->
<!--                  <div-->
<!--                    class="flex flex-center text-center bg-color-FD346E box-item-md"-->
<!--                  >-->
<!--                    挖掘商家的创业经历，突出店铺的发展历史和文化，在叙述产品的同时讲述不为人知的隐秘故事，抓住用户的眼球。-->
<!--                  </div>-->
<!--                  <div-->
<!--                    class="flex flex-center text-center bg-color-6001D3 box-item-sm q-ml-8"-->
<!--                  >-->
<!--                    无论怎样的合作方式，都是建立在三方信任的基础上。-->
<!--                  </div>-->
<!--                </div>-->
<!--                <div class="flex flex-direction-horizontal q-mt-8">-->
<!--                  <div-->
<!--                    class="flex flex-center text-center bg-color-6001D3 box-item-sm text-caption"-->
<!--                  >-->
<!--                    聚焦本土化、细化目标人群是探店博主发展的方向之一。-->
<!--                  </div>-->
<!--                  <div-->
<!--                    class="flex flex-center text-center bg-color-6001D3 box-item-sm q-ml-8"-->
<!--                  >-->
<!--                    相关部门与平台的正确监督，未来的用户观感会更好。-->
<!--                  </div>-->
<!--                  <div-->
<!--                    class="flex flex-center text-center bg-color-6001D3 box-item-sm q-ml-8"-->
<!--                  >-->
<!--                    《互联网广告管理办法（公开征求意见稿）》-->
<!--                  </div>-->
<!--                </div>-->
<!--              </div>-->
<!--            </div>-->
<!--          </div>-->
<!--        </div>-->
      </div>
      <div class="col-6">
        <div class="col module-container" style="position: absolute; top: -5px; left: 300px">
          <div class="row flex-center-vertical" style="color: #0d2436; position: center">
            <q-icon name="watch_later" size="24px" style="position: absolute; left: 200px; margin-top: 10px"/>
            <div style="position: absolute; left: 230px; margin-top: 10px">阶段计时器</div>
          </div>
          <div class="row flex" style="justify-content: space-between;margin-top: 25px;padding-left: 12px;padding-right: 12px;color: #0d61fe;">
            <div
              class="text-h3 row"
              style="
                padding: 12px;
                border: 1px solid #cccccc;
                box-sizing: border-box;
                border-radius: 8px;
              "
            >
              <div>{{ timer.tasks[timer.index].h }}</div>
              <div
                class="text-subtitle1"
                style="margin-right: 12px; position: relative"
              >
                <div style="position: absolute; bottom: 0">h</div>
              </div>
            </div>
            <div
              class="text-h3 row flex-center"
              style="margin-left: 12px; margin-right: 12px"
            >
              :
            </div>
            <div
              class="text-h3 row"
              style="
                padding: 12px;
                border: 1px solid #cccccc;
                box-sizing: border-box;
                border-radius: 8px;
              "
            >
              <div>{{ timer.tasks[timer.index].m }}</div>
              <div
                class="text-subtitle1"
                style="margin-right: 12px; position: relative"
              >
                <div style="position: absolute; bottom: 0">m</div>
              </div>
            </div>
            <div
              class="text-h3 row flex-center"
              style="margin-left: 12px; margin-right: 12px"
            >
              :
            </div>
            <div
              class="text-h3 row"
              style="
                padding: 12px;
                border: 1px solid #cccccc;
                box-sizing: border-box;
                border-radius: 8px;
              "
            >
              <div>{{ timer.tasks[timer.index].s }}</div>
              <div
                class="text-subtitle1"
                style="margin-right: 12px; position: relative"
              >
                <div style="position: absolute; bottom: 0">s</div>
              </div>
            </div>
            <q-btn
              flat
              :icon="timer.state ? 'stop' : 'play_arrow'"
              size="28px"
              @click="onClock"
              style="
                margin-left: 24px;
                color: #0d61fe;
                background: #ffffff;
                border: 1px solid #cccccc;
                border-radius: 8px;
              "
            />
          </div>
        </div>
        <div class="col module-container" style="position: absolute; top: -5px; left: 850px;width: 400px;height: 127px;">
          <div class="row flex-center-vertical" style="color: #0d2436; position: center">
            <q-icon name="mic" size="24px" style="position: absolute; left: 200px; margin-top: 10px;margin-left: -40px;"/>
            <div style="position: absolute; left: 230px; margin-top: 10px;margin-left: -40px;">录音控制器</div>
          </div>
          <div class="row flex flex-center-vertical"
               style="justify-content: space-between;margin-top: 12px;padding-left: 12px;padding-right: 12px;padding-top: 28px">
            <q-btn unelevated rounded color="green" :disable="state===1" @click="onRecordStart"
                   :label="state ===2 ?'恢复录音':'开始录音'" size="12px"
                   style="margin-top: 12px;padding: 8px 32px;"/>
            <q-btn unelevated rounded color="gray-light" :disable="state!==1" @click="onRecordPause" label="暂停"
                   size="12px"
                   style="margin-top: 12px;padding: 8px 32px;"/>
            <q-btn unelevated rounded color="tab" label="结束讨论" :disable="state!==1" size="12px"
                   style="margin-top: 12px;padding: 8px 32px;"/>
          </div>
        </div>
        <div
          class="col q-mt-xl module-container"
          style="
            position: absolute;
            left: 30px;
            top: 110px;
            right: 600px;
            width: 800px;
            height: 500px;
          "
        >
          <div class="row flex-center-vertical">
            <div style="margin-left: 12px; margin-top: 24px; color: #0d2436">
              小组互动频率
            </div>
            <div style="margin-left: 360px; margin-top: 24px; color: #0d2436">
              成员贡献时长
            </div>
          </div>
          <div
            class="row flex flex-center-vertical"
            style="
              justify-content: space-between;
              margin-top: 12px;
              padding-left: 12px;
              padding-right: 12px;
            "
          >
            <q-img :src="url" />
          </div>
        </div>
      </div>
      <q-dialog v-model="model1" class="text-black" persistent>
        <q-card class="dialog-switch-card-container">
          <q-card-section class="row flex flex-center">
            <div class="text-h6">为本次讨论命名</div>
          </q-card-section>
          <q-card-section class="row flex flex-center" v-show="model1_error">
            <span style="color: red">讨论名称重复，请更换</span>
          </q-card-section>
          <q-card-section>
            <q-input
              white
              v-model="text"
              label="输入讨论名称"
              autofocus
              error-message="讨论名称不能为空！"
              :error="!isValid"
            />
          </q-card-section>

          <q-card-actions align="right" class="dialog-switch-card-content4">
            <q-btn
              unelevated
              rounded
              color="blue"
              @click="onCreateDiscussion"
              label="确认"
              size="12px"
              class="dialog-switch-card-content4-button"
            />
          </q-card-actions>
        </q-card>
      </q-dialog>
      <q-dialog v-model="model2" position="bottom" persistent>
        <q-card dark class="dialog-switch-card-container">
          <q-card-section class="row items-center">
            <div class="text-h6" style="color: #192431">时间到！</div>
            <q-space />
            <q-btn
              round
              dense
              flat
              icon="hourglass_top"
              :disable="!timer.canAddTime"
              @click="model3 = true"
            />
          </q-card-section>
          <q-card-section>
            <div class="text-subtitle2" style="color: #192431; position:absolute;height: 300px">
              休息一下，准备进入下一个阶段吧！
            </div>
          </q-card-section>
          <div class="dialog-switch-spilt-line" />
          <q-card-actions class="row items-center q-mb-8">
            <q-icon
              name="tips_and_updates"
              color="blue"
              style="font-size: 1.5rem"
            />
            <q-space />
            <q-btn
              unelevated
              rounded
              color="dark"
              @click="onNextTask"
              label="NEXT STAGE"
              size="12px"
            />
          </q-card-actions>
        </q-card>
      </q-dialog>
      <q-dialog v-model="model3" position="bottom" persistent>
        <q-card dark class="dialog-switch-card-container">
          <q-card-section class="row items-center">
            <div class="text-h6" style="color: #192431">时间到！</div>
            <q-space />
            <q-btn round dense flat icon="hourglass_top" />
          </q-card-section>
          <q-card-section>
            <div class="text-subtitle2" style="color: #192431">
              可以选择以下延长时间，之后再进行下一轮任务。
            </div>
            <div
              class="flex flex-direction-horizontal flex-center-vertical q-px-xl q-mt-lg"
              style="justify-content: space-between"
            >
              <div>延长：</div>
              <q-radio dark v-model="mode" val="1" label="1分钟" />
              <q-radio dark v-model="mode" val="3" label="3分钟" />
              <q-radio dark v-model="mode" val="5" label="5分钟" />
            </div>
          </q-card-section>
          <div class="dialog-switch-spilt-line" />
          <q-card-actions class="row items-center q-mb-8">
            <q-space />
            <q-btn
              unelevated
              rounded
              color="pink"
              @click="onAddTime"
              label="确认"
              size="12px"
            />
          </q-card-actions>
        </q-card>
      </q-dialog>
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import Recorder from "js-audio-recorder";
import { createDiscussion, getRecords, upload } from "src/request/api";

let recorder = new Recorder({
  sampleBits: 16,
  sampleRate: 48000,
  numChannels: 1,
});

export default defineComponent({
  name: "PageIndex",
  data: () => ({
    model1: true,
    model1_error: false,
    model2: false,
    model3: false,
    mode: "1",
    text: "",
    isValid: false,
    state: 0, // 状态0：未开始 状态1：正在录音 状态2：暂停
    timeProgress: 0,
    refreshTime: 10,
    uploadTime: 600,
    url: "",
    timer: {
      index: 0,
      state: false,
      interval: null,
      canAddTime: true,
      tasks: [
        {
          h: "00",
          m: "30",
          s: "05",
        },
        {
          h: "00",
          m: "15",
          s: "05",
        },
        {
          h: "00",
          m: "30",
          s: "05",
        },
        {
          h: "00",
          m: "30",
          s: "05",
        },
        {
          h: "00",
           m: "00",
           s: "10",
         },
         {
           h: "00",
           m: "00",
           s: "10",
         },
      ],
    },
  }),
  methods: {
    onCreateDiscussion() {
      if (this.text === "") {
        this.isValid = false;
      } else {
        this.isValid = true;
        const data = {
          name: this.text,
        };
        createDiscussion(JSON.stringify(data)).then((res) => {
          if (res.data.code === 1) {
            this.model1 = false;
          } else {
            this.model1_error = true;
            // 连接失败
          }
        });
      }
    },
    onRecordStart() {
      if (this.state === 0) {
        recorder.start().then(
          () => {
            this.state = 1;
            // 开始录音
          },
          (error) => {
            // 出错了
            console.log(error);
          }
        );
      } else if (this.state === 2) {
        this.state = 1;
        recorder.resume();
      }
    },
    onRecordPause() {
      this.state = 2;
      recorder.pause();
    },
    onRecordStop() {
      this.state = 0;
      recorder.stop();
    },
    onRefresh() {
      setInterval(() => {
        setTimeout(() => {
          this.url = "";
          this.url =
            "http://123.207.237.143:3308/results/" +
            this.text +
            "/img/result.jpg" +
            "?t=" +
            Math.random();
          // this.url = 'http://localhost:3308/results/' + this.text + '/img/result.jpg' + "?t=" + Math.random()
          getRecords(this.text).then((res) => {
            // console.log(eval(res.data.message).length)
          });
        }, 0);
      }, parseInt(this.refreshTime) * 1000);
    },
    initializeClock(endTime) {
      this.interval = setInterval(() => {
        const total = endTime - Date.now();
        if (total <= 0) {
          this.model2 = true;
          clearInterval(this.interval);
        } else {
          const seconds = Math.floor((total / 1000) % 60);
          const minutes = Math.floor((total / 1000 / 60) % 60);
          const hours = Math.floor((total / (1000 * 60 * 60)) % 24);
          this.timer.tasks[this.timer.index].h = ("0" + hours).slice(-2);
          this.timer.tasks[this.timer.index].m = ("0" + minutes).slice(-2);
          this.timer.tasks[this.timer.index].s = ("0" + seconds).slice(-2);
        }
      }, 100);
    },
    onClock() {
      if (this.timer.state) {
        this.timer.state = false;
        clearInterval(this.interval);
      } else {
        this.timer.state = true;
        const hours = parseInt(this.timer.tasks[this.timer.index].h);
        const minutes = parseInt(this.timer.tasks[this.timer.index].m);
        const seconds = parseInt(this.timer.tasks[this.timer.index].s);
        this.initializeClock(
          Date.now() +
            seconds * 1000 +
            minutes * 60 * 1000 +
            hours * 60 * 60 * 1000
        );
      }
    },
    onNextTask() {
      this.timer.index++;
      this.model2 = false;
      this.timer.canAddTime = true;
      this.onClock();
      this.onClock();
    },
    onAddTime() {
      this.timer.canAddTime = false;
      const m =
        parseInt(this.timer.tasks[this.timer.index].m) + parseInt(this.mode);
      this.timer.tasks[this.timer.index].m = ("0" + m).slice(-2);
      this.model2 = false;
      this.model3 = false;
      this.onClock();
      this.onClock();
    },
  },
  created() {
    const that = this;
    recorder.onprogress = function (params) {
      that.timeProgress = parseInt(params.duration.toString());
    };
    that.onRefresh();
    this.$watch("timeProgress", function (newValue) {
      if (parseInt(newValue) === parseInt(that.uploadTime)) {
        recorder.stop();
        const wav = recorder.getWAVBlob();
        let formData = new FormData();
        formData.append("file", wav);
        formData.append("name", that.text);
        upload(formData);
        recorder.start();
      }
    });
  },
});
</script>
<style lang="scss" scoped>
.box-container {
  color: #ffffff;
  box-sizing: border-box;
  box-shadow: 0 10px 29px 0 rgba(68, 88, 144, 0.1);
  border-radius: 10px;
}

.box-progress-bar {
  color: #0d61fe;
  right: 32px;
  position: absolute;
  width: 120px;
}

.box-item-sm {
  width: 160px;
  height: 80px;
  padding: 10px;
  margin-left: 10px;
  margin-bottom: 10px;
  border-radius: 3px;
}

.box-item-md {
  width: 288px;
  height: 80px;
  padding: 10px;
  margin-left: 10px;
  margin-bottom: 10px;
  border-radius: 3px;
}

.box-item-mz {
  width: 368px;
  height: 80px;
  padding: 20px;
  margin-left: 10px;
  margin-bottom: 10px;
  border-radius: 3px;
}

.box-item-lg {
  width: 140px;
  height: 168px;
  padding: 10px;
}

.box-item-xl {
  width: 260px;
  height: 168px;
  padding: 10px;
}

.module-container {
  border-radius: 20px;
  background: #fff;
  padding: 12px;
  box-shadow: 0 10px 29px 0 rgb(68 88 144 / 10%);
  border-radius: 10px;
}

.dialog-switch-card-container {
  background-color: #ffffff;
  width: 480px;
}

.dialog-switch-spilt-line {
  margin-top: 10px;
  margin-bottom: 10px;
  border-top: 1px solid #707070;
}
</style>
