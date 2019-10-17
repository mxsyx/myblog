{% extends "play/playbase.tpl" %}
{% load tplfilter %}

{% block breadcrumb %}
<!-- 站点导航 -->
<div class="container">
  <ul class="breadcrumb">
    <li><a href="/">首页</a></li>
    <li><a href="/classify/type/15/time/0/area/0/page/0">动漫</a></li>
    <li><a href="/classify/type/{{ info.flag_type|custom_type_to_num }}/time/0/area/0/page/0">{{ info.flag_type}}</a></li>
    <li class="active"><a href="/info/anime/{{ info.id }}">{{ info.name }}</a></li>
  </ul>
</div>
{% endblock %}

{% block play %}
<!-- 播放容器 -->
<div class="container" id="container-play">
  <div class="prism-player" id="player-con"></div>
  <form style="display:none" id="cipher-form">
  {% csrf_token %}
    <input type="hidden" name="cipher" value="{{ url }}">
  </form>
</div>
</div>
{% endblock %}

{% block playurl %}
<!-- 播放线路容器 -->
<div class="container" id="container-playurl">
  <h3>播放线路
    <a href="/play/anime/{{ info.id }}/{{ next_episode }}" class="pn pull-right">【下一集】</a>
    <a href="/play/anime/{{ info.id }}/{{ previous_episode }}" class="pn pull-right">【上一集】</a>
  </h3>
  <ul class="itemlist">
    {% for num in nums %}
    {% if forloop.counter == episode %}
    <li id="itemlist-li-active">
      <a href="/play/anime/{{ info.id }}/{{forloop.counter}}">第{{forloop.counter}}集</a>
    </li>
    {% else %}
    <li>
      <a href="/play/anime/{{ info.id }}/{{forloop.counter}}">第{{forloop.counter}}集</a>
    </li>
    {% endif %}
    {% endfor %}
  </ul>
</div>
{% endblock %}
