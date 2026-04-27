# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_git80
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


#include <iostream>
using namespace std;
int main(){
	int n,s=1;
	cin>>n;
	int a[n];
	for(int i=0;i<n;i++) cin>>a[i];
	for(int i=1;i<n;i++){
		if(a[i]!=a[i-1]) s++;
	}
	cout<<s;
}
