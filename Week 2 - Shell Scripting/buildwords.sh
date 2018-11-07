#! /bin/bash

#----------------------------------------
#  buildwords.sh
#  CS35L/Week2
#
#  Created by Jayant Mehra on 1/22/18
#
#----------------------------------------

#From the first argument, grab all lines which have <td> in them
grep "<td>" $1 |

#Only output the even numbered lines
sed -n "n;p" |

#Convert all uppercase letters to lowercase
tr [:upper:] [:lower:] |

#Replace <u> with nothing
sed "s/<u>//g" |

#Replace </u> with nothing
sed "s/<\/u>//g" |

#Replace the okina(`) with apostrophe (')
sed "s/\`/\'/g" |

#Replace <td> with nothing
sed "s/<td>//g" |

#Replace </td> with nothing
sed "s/<\/td>//g" |

#Replace ,SPACE with new line
sed "s/, /\n/g" |

#Remove all the leading space
sed "s/^    //g" |

#If a word contains non-Hawaiian letters, delete it
sed "/[bcdfgjqrstvxyz0-9\? -]/d" |

#Sort it and remove the duplicates
sort -u |

#Remove empty lines
sed '/^$/d'
