# Copyright 2013 David Marin
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""usage:
URL="http://stoprush.net/json_2.php?flag=all&type=a"
DATA="page=1&rp=50000&sortname=date_last_reported&sortorder=asc&query=&qtype="
curl -X POST $URL -d $DATA > stoprush.json
python -m pbg.stoprush.stoprush < stoprush.json
"""
