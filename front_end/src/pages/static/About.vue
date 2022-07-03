<template>
  <q-page class="flex flex-center-vertical flex-direction-vertical">
    <div class="text-h6 page-title1">TEAM MEMBERS</div>
    <div class="text-h2 text-weight-medium text-center page-title2">
      团队成员
    </div>
    <div class="text-body2 page-title3 text-center">
      任务切换策略在设计领域的相关研究<br />
      我们来自呼啦圈服务设计工作室
    </div>
    <div class="row member-line-container">
      <div class="col text-white text-center member-container">
        <q-avatar size="210px">
          <img src="../../assets/avatar1.png" />
        </q-avatar>
        <div class="text-body1 member-name">胡莹</div>
        <div class="text-body2 member-info">任务切换策略研究指导教师</div>
      </div>
      <div class="col text-white text-center member-container">
        <q-avatar size="210px">
          <img src="../../assets/avatar2.png" />
        </q-avatar>
        <div class="text-body1 member-name">杜星</div>
        <div class="text-body2 member-info">任务切换策略研究人员</div>
      </div>
    </div>
    <div class="row member-line-container">
      <div class="col text-white text-center member-container">
        <q-avatar size="210px">
          <img src="../../assets/avatar5.png" />
        </q-avatar>
        <div class="text-body1 member-name">白一茗</div>
        <div class="text-body2 member-info">任务切换策略研究人员</div>
      </div>
      <div class="col text-white text-center member-container">
        <q-avatar size="210px">
          <img src="../../assets/avatar7.png" />
        </q-avatar>
        <div class="text-body1 member-name join-info">加入我们</div>
      </div>
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "PageIndex",
  methods: {},
});
</script>
<style lang="scss" scoped>
.page-title1 {
  color: #fd346e;
  margin-top: 96px;
}

.page-title2 {
  line-height: 1.5;
  color: #fff;
  margin-top: 27px;
}

.page-title3 {
  display: flex;
  color: #fbfbfb;
  margin-top: 13px;
  align-items: center;
  line-height: 1.5rem;
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

.member-line-container {
  margin-top: 60px;
}

.member-container {
  margin-left: 40px;
  margin-right: 40px;
}

.member-name {
  margin-top: 40px;
}

.member-info {
  margin-top: 10px;
}

.join-info {
  margin-top: 40px;
  text-decoration: underline;
}
</style>
