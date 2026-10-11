# -*- coding: utf-8 -*-
"""从 index.html 生成手机纯文字版：移除所有图片区块，保留全部文字信息。"""
import re, os

src = r'H:/hermes-xiangmu/宜昌自驾攻略/index.html'
html = open(src, encoding='utf-8').read()

# 1) 移除所有图片区块 <div class="gal">…</div> / <div class="gal three">…</div>
html2, n = re.subn(
    r'<div class="gal(?: three)?">\s*(?:<figure>.*?</figure>\s*)+</div>\s*',
    '', html, flags=re.S)

# 2) 概览里「五个地方长什么样」下面原本是图，换成文字一览
old = '<h3>五个地方长什么样</h3>'
new = ('<h3>五个地方一句话</h3>\n'
       '  <div class="box">\n'
       '    <ul>\n'
       '      <li><b>三峡大坝</b>（必去 · Day2）：坛子岭俯瞰全景、185 平台平视坝顶 —— 高峡出平湖</li>\n'
       '      <li><b>G348 三峡公路</b>（必去 · Day1）：39.6 km 沿江画廊，9 个观景台随停随拍</li>\n'
       '      <li><b>三峡人家</b>（必去 · Day3）：龙进溪、巴王寨、土家婚俗表演</li>\n'
       '      <li><b>三峡大瀑布</b>（加游 · Day2 下午）：高 102 米、宽 80 米，能「穿瀑」走过去</li>\n'
       '      <li><b>三峡移民博物馆</b>（加游 · Day2，免费）：秭归「水下归州」展厅</li>\n'
       '    </ul>\n'
       '  </div>')
if old in html2:
    html2 = html2.replace(old, new)
    print('概览图片标题 -> 文字一览：OK')
else:
    print('!! 未找到概览标题，跳过')

# 3) 页脚标注这只是文字版
html2 = html2.replace('政策与价格以景区当日公告为准',
                      '手机文字版（无图）· 政策与价格以景区当日公告为准')

# 4) 标题也标一下
html2 = html2.replace('<title>方略肖邦直捣三峡坝 · 长沙→宜昌3天2晚自驾</title>',
                      '<title>方略肖邦直捣三峡坝 · 手机版</title>')

out = r'C:/Users/Administrator/Desktop/宜昌攻略-手机版.html'
open(out, 'w', encoding='utf-8').write(html2)

print('移除图片区块数:', n)
print('残留 <img> 标签:', html2.count('<img'))
print('文件大小: %.1f KB' % (os.path.getsize(out) / 1024))
print('关键内容检查 -> 三峡移民博物馆: %d 处 / 陶珠路: %d 处 / 应急电话: %d 处'
      % (html2.count('三峡移民博物馆'), html2.count('陶珠路'), html2.count('应急电话')))
