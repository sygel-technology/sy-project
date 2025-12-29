- Since v18, the behaviour of this module is different.

  The reason is that, in the base project module, the "kanban_state" field has been removed from the project.task model, and has been replaced with the "state" field, which does not longer contain the "blocked" value. 

  The old "blocked" state came along with some UI customization to warn the user of that state. The new "waiting" state of the new v18 field has been used to replace this UI behaviour, as it can express the same as the old blocked state. 

  A new button has been added to block tasks and assign that "waiting" state.

- The module’s manual blocking mechanism currently operates in parallel with Odoo’s native Blocked by feature.

  IMP: As a future improvement, it could be explored to better synchronize both mechanisms. For example, disabling or hiding the manual Block/Unblock actions when a task is already blocked by native dependencies, or automatically enabling/disabling the manual blocking state when blocking dependencies (depend_on_ids field) are added or removed.

  This could be considered only if it can be implemented without introducing excessive complexity or altering the current lightweight behavior of the module.
