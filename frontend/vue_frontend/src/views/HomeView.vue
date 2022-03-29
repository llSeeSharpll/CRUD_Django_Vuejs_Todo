<template>
  <div class="home">
    <h1 class="text-center">Todo List</h1>
    <b-table :items="tasks" :fields="fields" striped responsive="sm">
      <template #cell(Description)="row"
        ><div v-if="!row.item.toggle">
          {{ row.item.Description.substring(0, 25) }}
        </div>
        <div v-if="row.item.toggle">{{ row.item.Description }}</div>
        <b-button
          size="sm"
          @click="row.item.toggle = !row.item.toggle"
          class="mr-2"
        >
          {{ row.item.toggle ? "Hide" : "Show" }} More Details
        </b-button>
      </template>
      <template #cell(Completed)="row"
        ><b-form-checkbox
          @change="Completed(row.index)"
          v-model="row.item.Completed"
        >
          <div class="p-2">Completed</div>
        </b-form-checkbox>
      </template>
      <template #cell(Remove)="row">
        <b-button
          variant="danger"
          size="sm"
          @click="remove(row.index)"
          class="mr-2"
        >
          Remove
        </b-button>
      </template>
    </b-table>
    <div v-if="!tasks.length" class="p-2 text-center">
      There is no current tasks in the todo list
    </div>
    <div class="text-center">
      <b-button v-b-modal.add-model variant="success">Add task</b-button>
    </div>
    <b-modal @ok="addtask()" id="add-model" title="Add Task">
      <template #modal-footer="{ cancel, ok }">
        <!-- Emulate built in modal footer ok and cancel button actions -->
        <b-button size="sm" variant="danger" @click="cancel()">
          Cancel
        </b-button>
        <b-button size="sm" variant="success" @click="ok()">
          Add Task
        </b-button>
      </template>
      <b-form-group
        id="fieldset-1"
        label="Enter task title and description"
        label-for="input-1"
      >
        <b-form-group
          label="Task: "
          label-for="nested-street"
          label-cols-sm="3"
          label-align-sm="right"
        >
          <b-form-input v-model="task.name" id="nested-street"></b-form-input>
        </b-form-group>
        <b-form-group
          label="Description: "
          label-for="nested-street"
          label-cols-sm="3"
          label-align-sm="right"
        >
          <b-form-input v-model="task.desc" id="nested-street"></b-form-input>
        </b-form-group>
      </b-form-group>
    </b-modal>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "HomeView",
  data() {
    return {
      fields: ["Task", "Description", "Completed", "Remove"],
      tasks: [],
      task: {
        name: "",
        desc: "",
      },
    };
  },
  mounted() {
    axios
      .get("/api/gettask")
      .then((respone) => {
        this.tasks = respone.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {
    async addtask() {
      await axios.post("/api/addtask", {
        title: this.task.name,
        description: this.task.desc,
      });
    },
    async remove(Index) {
      await axios.delete("/api/deletetask", { data:{id: this.tasks[Index].id} });
      this.tasks.splice(Index, 1);
    },
    async Completed(Index) {
      await axios.patch("/api/updatetaskstatus", { id: this.tasks[Index].id });
    },
  },
};
</script>
