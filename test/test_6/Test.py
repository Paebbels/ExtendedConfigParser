# EMACS settings: -*-	tab-width: 2; indent-tabs-mode: t; python-indent-offset: 2 -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
#
# ==============================================================================
# Authors:          Patrick Lehmann
#
# Python Test:      Undocumented
#
# Description:
# ------------------------------------
# Undocumented
#
# License:
# ==============================================================================
# Copyright 2007-2016 Patrick Lehmann - Dresden, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
#
from test import BaseTest

class Test(BaseTest):
	@staticmethod
	def GetName():
		return "test_6"
	
	@staticmethod
	def GetFiles():
		return [
			"test.ini"
		]
	
	@staticmethod
	def GetExpected():
		return {
			"PRE.section_1": {
				"option_1_1": "value_1_1",
				"option_1_2": "value_2_2",
				"option_1_3": "value_2_3",
				"option_1_4": "value_1_4",
				"option_1_5": "value_2_5",
				"option_1_6": "value_2_6"
			}
		}
