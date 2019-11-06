import crypto from 'crypto';

/**
 * 加密字符串
 * @param content 需要加密的内容
 * @param salt    盐值
 * @param method  加密方式(默认sha256)
 * @param encode  编码方式(默认base64)
 * @returns 加密后的结果
 */
function encrypt(content, salt, method='sha256', encode='base64') {
  const hash = crypto.createHash(method);
  const result  = hash.update(`${content}${salt}`).digest(encode);
  return result;
}

export { encrypt };
