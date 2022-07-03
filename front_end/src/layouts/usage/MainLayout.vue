<template>
  <q-layout class="q-main-root">
    <q-header>
      <q-toolbar class="toolbar">
        <q-avatar square size="48px">
          <q-img src="../../assets/logo.png" />
        </q-avatar>
      </q-toolbar>
    </q-header>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "MainLayout",
  data: () => ({
    homeClass: ["text-weight-bolder", "toolbar-menu-active"],
    switchClass: ["text-weight-bolder", "toolbar-menu-inactive"],
    otherToolsClass: ["text-weight-bolder", "toolbar-menu-inactive"],
    aboutClass: ["text-weight-bolder", "toolbar-menu-inactive"],
  }),
  methods: {
    toOtherToolsLink() {
      window.open("https://servicedesignheuristiccards.com.cn/#");
    },
    toAbout(path) {
      this.$router.push(path);
      switch (path) {
        case "/about":
          this.homeClass[1] = "toolbar-menu-inactive";
          this.aboutClass[1] = "toolbar-menu-active";
          break;
        case "/":
          this.homeClass[1] = "toolbar-menu-active";
          this.aboutClass[1] = "toolbar-menu-inactive";
          break;
      }
    },
  },
});
</script>
<style lang="scss" scoped>
.q-main-root {
  background-color: #e8f2ff;
}

.toolbar {
  background-color: #ffffff;
  padding-top: 27px;
  padding-left: 140px;
  padding-right: 160px;
}

.toolbar-logo-container {
  color: white;
  height: 48px;
  line-height: 2rem;
}

.toolbar-logo-subtitle {
  font-size: 0.5rem;
  line-height: 1.5rem;
}

.toolbar-menu-inactive {
  color: #abafc7;
}

.toolbar-menu-active {
  color: white;
}

.footer-right-about {
  margin-top: 32px;
}

.footer-container {
  margin-top: 64px;
  background: #0d2436;
  height: 420px;
  width: 100%;
}

.footer-left-container {
  margin-left: 108px;
  margin-top: 81px;
}

.footer-left-icon {
  margin-right: 12px;
}

.footer-left-text {
  color: white;
  margin-top: 32px;
  line-height: 1.5rem;
}

.footer-left-copyright {
  color: white;
  margin-top: 64px;
}

.footer-right-container {
  margin-top: 81px;
}

.footer-right-contact-container {
  margin-top: 32px;
}

.footer-right-contact-text {
  margin-left: 16px;
}

.toolbar-menu-other-tools-link {
  min-width: 28px;
}
</style>
