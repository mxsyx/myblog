<!-- 通用模态框 -->
<template>
  <div class="modal modal-top" v-bind:class="{show: showModal}">
    <header>
      <span>{{ modalTip }}</span>
      <i class="fa fa-times" aria-hidden="true" v-on:click="closeModal"></i>
    </header>
    <div>
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  props: ['modalTip'],

  data: function() {
    return {
      position: 'center',
      showModal: false,
      hasHeader: true,
    }
  },

  methods: {
    openModal() {
      this.showModal = true;
    },

    closeModal() {
      this.showModal = false;
    }
  }
}
</script>

<style scoped>
.modal {
  max-height: 0px;
  position:fixed;
  width: 100%;
  background-color: #fff;
  transition: all 0.5s linear;
}

.modal-top {
  top: 100%;
  left: 0px;
  transform: translateY(-100%);
}

.modal header {
  padding: 0.5rem;
  border-top: solid 1px #ccc;
  border-bottom: solid 1px #ccc;
}

.modal header span {
  font-size: 0.7rem;
  font-weight: 700;
}

.modal header i {
  float: right;
  margin-right: 5px;
  cursor: pointer;
  opacity: 0.6;
}
.modal header i:hover {
  opacity: 1;
}

.modal > div {
  padding: 0.5rem;
}

.show {
  max-height: 150px;
}

</style>