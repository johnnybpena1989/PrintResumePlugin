import os
import json
import octoprint.plugin

class PrintResumePlugin(octoprint.plugin.StartupPlugin,
                        octoprint.plugin.EventHandlerPlugin,
                        octoprint.plugin.TemplatePlugin):
    
    def on_after_startup(self):
        self.saved_states_dir = os.path.join(self._basefolder, "paused_jobs")
        if not os.path.exists(self.saved_states_dir):
            os.makedirs(self.saved_states_dir)
        self._logger.info("Print Resume Plugin Initialized.")
    
    def on_event(self, event, payload):
        if event == "PrintPaused":
            self.save_print_state()
        elif event == "PrintResumed":
            self._logger.info("Print resumed.")

    def save_print_state(self):
        state = {
            "position": self._printer.get_current_data()["progress"]["printTimeLeft"],
            "current_position": self._printer.get_current_position(),
            "temperatures": self._printer.get_current_temperatures(),
        }
        job_name = self._printer.get_current_job()["file"]["name"]
        save_path = os.path.join(self.saved_states_dir, f"{job_name}.json")
        
        with open(save_path, "w") as f:
            json.dump(state, f)
        self._logger.info(f"Print state saved: {save_path}")
    
    def load_print_state(self, job_name):
        save_path = os.path.join(self.saved_states_dir, f"{job_name}.json")
        if not os.path.exists(save_path):
            self._logger.error(f"No saved state for {job_name}")
            return None
        with open(save_path, "r") as f:
            return json.load(f)

    def get_template_configs(self):
        return [
            dict(type="tab", name="Resume Print", template="resume_print_tab.jinja2")
        ]
