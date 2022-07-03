/**
 * 上传音频
 */
import { post, get } from "src/request/request";

export async function upload(data) {
  return await post("http://123.207.237.143:3308" + "/api/v1/record", data);
  // return await post('http://localhost:3308' + '/api/v1/record', data)
}

/**
 * 添加测试
 */
export async function createDiscussion(data) {
  return await post("http://123.207.237.143:3308" + "/api/v1/name", data);
  // return await post('http://localhost:3308' + '/api/v1/name', data)
}

/**
 * 获得待处理录音数量
 */
export async function getRecords(name) {
  return await get(
    "http://123.207.237.143:3308" + "/api/v1/record?name=" + name
  );
  // return await get('http://localhost:3308' + '/api/v1/record?name=' + name)
}
