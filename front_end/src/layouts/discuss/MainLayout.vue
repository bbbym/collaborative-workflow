<template>
  <q-layout class="q-main-root text-white">
    <div class="col">
      <div class="q-pa-md row"></div>
      <div class="col">
        <q-page-container>
          <router-view />
        </q-page-container>
      </div>
    </div>
  </q-layout>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "MainLayout",
  data: () => ({}),
  methods: {
    toHome() {
      this.$router.push("/");
    },
    toUsage() {
      this.$router.push("/usage");
    },
  },
});
</script>
<style lang="scss" scoped>
.q-main-root {
  background-color: #e8f2ff;
}

.logo-icon {
  margin-right: 12px;
}

.logo-text-container {
  color: #081420;
  height: 48px;
  line-height: 2rem;
}

.logo-subtitle {
  font-size: 0.5rem;
  line-height: 1.5rem;
}

.list-container {
  margin-left: 12px;
  margin-right: 12px;
  padding: 12px;
  border-radius: 10px;
  background: #081420;
}

.list-tips-text {
  margin-top: 24px;
  color: #abafc7;
}

.list-menu-container {
  margin-top: 24px;
}

.list-menu-item1 {
  border-radius: 10px;
  background: #081420;
  width: 28px;
  height: 28px;
  margin-right: 12px;
}

.list-menu-item2 {
  border-radius: 10px;
  background: #081420;
  width: 28px;
  height: 28px;
  margin-right: 12px;
}

.list-menu-item3 {
  border-radius: 10px;
  background: #081420;
  width: 28px;
  height: 28px;
  margin-right: 12px;
}

.top-search-container {
  margin-left: 24px;
  margin-top: 28px;
  width: 600px;
}

.top-search-icon {
  color: #abafc7;
}

.top-menu-container {
  border-radius: 10px;
  background: #081420;
  margin-right: 36px;
  margin-left: auto;
}

.top-menu-item {
  margin-left: 8px;
  margin-right: 8px;
}
</style>
