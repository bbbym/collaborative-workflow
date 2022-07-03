const routes = [
  {
    path: "/",
    component: () => import("layouts/static/MainLayout.vue"),
    children: [
      { path: "", component: () => import("pages/static/Index.vue") },
      { path: "about", component: () => import("pages/static/About.vue") },
    ],
  },
  {
    path: "/usage/",
    component: () => import("layouts/usage/MainLayout.vue"),
    children: [
      { path: "/usage/", component: () => import("pages/usage/Index.vue") },
      {
        path: "/discussion/",
        component: () => import("pages/usage/MyDiscussion.vue"),
      },
      { path: "/usageOld/", component: () => import("pages/usage/Index2.vue") },
    ],
  },
  {
    path: "/discuss/",
    component: () => import("layouts/discuss/MainLayout.vue"),
    children: [
      { path: "/discuss/", component: () => import("pages/discuss/Index.vue") },
    ],
  },
];

export default routes;
