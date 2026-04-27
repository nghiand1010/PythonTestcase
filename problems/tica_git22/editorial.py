# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_git22
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


#include <bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int n,s,k=0;
	cin>>n>>s;
	int a[n];
	for(int i=0;i<n;i++) cin>>a[i];
	sort(a,a+n);
	for(int i=n-1;i>=0;i--){
		int x=s/a[i];
		s-=a[i]*x;
		k+=x;
	}
	cout<<k;
}
